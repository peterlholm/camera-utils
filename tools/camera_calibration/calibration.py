"camera calibration"
from pathlib import Path
import numpy as np
import cv2 as cv

# pylint: disable=too-many-arguments,too-many-locals, too-many-branches, too-many-statements
_DEBUG = False
_INFO = True
_CV2 = True     # use simple CV2 example

def save_camera_matrix(filename, mtx, dist, rvecs=None, tvecs=None, optmtx=None ):
    "Save the camera matrix set"
    np.savez(filename, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs, optmtx=optmtx )
    #np.savetxt("test", mtx)

def read_camera_matrix(filename):
    "read the camera matrix set"
    arrfile = np.load(filename, allow_pickle=True)
    #print(arrfile)
    return arrfile['mtx'], arrfile['dist'], arrfile['optmtx'], arrfile['rvecs'], arrfile['tvecs']

def get_optimal_camera_matrix(mtx, dist, size, alfa=1):
    "create optimal matrix alfa=0.0 crop picture alfa=1.0 retain all"
    #h,  w = img.shape[:2]
    h, w = size
    #print(size, w, h)
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), alfa, (w,h))
    if _DEBUG:
        print("New matrix", newcameramtx)
        print("ROI", roi)
    return newcameramtx, roi

def undistort(img, mtx, dist, alfa=1):
    "undistort an image alfa=0.0 crop picture alfa=1.0 retain all "
    #img = cv.imread(str(pic1))
    #img = cv.imread(FOLDER +'my/color1.jpg')
    h,  w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), alfa, (w,h))
    print("newcameramtx", newcameramtx)
    print("roi", roi)
    np.save("trans.npy", newcameramtx)
    # undistort
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv.imshow("org", img)
    cv.imshow("result", dst)
    cv.waitKey(15000)
    cv.destroyAllWindows()
    return dst

def undistort_pic(file, mtxfile):
    "undistort picture from file returning img"
    img = cv.imread(str(file))
    mtx, dist, optmtx, rvec, tvec = read_camera_matrix(mtxfile) # pylint: disable=unused-variable
    img2 = undistort(img, mtx, dist)
    return img2

def calibrate_camera(folder, chessboard=(6,8)):
    "calibrate by all jpg files in folder and used with a chess board gridx x gridy returning cameramatrix and distcoeffs "
    # number point with full black corners
    if not Path(folder).exists():
        raise FileNotFoundError("The folder does not exist")

    # opencv images use 7 x 6 grid
    gridx = chessboard[0]
    gridy = chessboard[1]
    # termination criteria
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((gridx*gridy,3), np.float32)
    #objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
    objp[:,:2] = np.mgrid[0:gridx,0:gridy].T.reshape(-1,2)
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    #find immages
    if _DEBUG:
        print("Folder:", folder)
        print("chessboard", chessboard)
    filemask = '*.jpg'
    images = folder.glob(filemask)
    no_pictures = 0
    ok_pictures = 0
    for fname in images:
        no_pictures += 1
        # if _DEBUG:
        #     print(fname)
        img = cv.imread(str(fname))
        if _CV2:
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        else:
            alpha = 2.5 # Contrast control (1.0-3.0)
            beta = 00 # Brightness control (0-100)
            img2 = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
            #img2 = cv.resize(img,(img.shape[1]//3,img.shape[0]//3), interpolation = cv.INTER_AREA)
            gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        if _DEBUG:
            cv.imshow("image",img)
            cv.imshow("gray",gray)
            cv.waitKey(1000)

        # Find the chess board corners
        if _CV2:
            #ret, corners = cv.findChessboardCorners(gray, (gridx,gridy), None, flags=cv.CALIB_CB_ADAPTIVE_THRESH )
            ret, corners = cv.findChessboardCorners(gray, (gridx,gridy), None)
        else:
            ret, corners = cv.findChessboardCornersSB(gray, (gridx,gridy), None)
            #ret, corners = cv.findChessboardCorners(gray, (7,7), None)

        # If found, add object points, image points (after refining them)
        if ret:
            if _DEBUG:
                print("Corners found in", fname)
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
            ok_pictures +=1
            if _DEBUG:
                # Draw and display the corners
                cv.drawChessboardCorners(img, (gridx,gridy), corners2, ret)
                cv.imshow(str(fname.name), img)
                pic1 = fname
                cv.waitKey(4500)
                cv.destroyWindow(str(fname.name))
        else:
            if _INFO:
                print("Kan ikke finde skakbræt i billed:", str(fname.name))
            if _DEBUG:
                #cv.imshow(str(fname.name), img)
                #cv.waitKey(5000)
                pass
        if _DEBUG:
            cv.waitKey(1500)
            cv.destroyAllWindows()
    if _DEBUG:
        #print("imgpoints", imgpoints)
        cv.destroyAllWindows()

    if len(objpoints)==0:
        return None,None

    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    if _DEBUG:
        print("reprojection error",ret)
        print("camera matrix",mtx)
        print('distortion', dist)
        print ('rotation vecs', rvecs)
        print("tranlation vecs", tvecs)

        img = cv.imread(str(pic1))
        h,  w = img.shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
        print("newcameramtx", newcameramtx)
        #print("roi", roi)
        # undistort
        dst = cv.undistort(img, mtx, dist, None, newcameramtx)
        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        cv.imshow("org", img)
        cv.imshow("result", dst)
        cv.waitKey(5000)
        cv.destroyAllWindows()
    print("Ok pictures:", ok_pictures, " Not found pictures", no_pictures-ok_pictures)
    return mtx, dist

if __name__ == "__main__":
    myfolder = Path(__file__).parent / 'testimages' / 'pizero/serie1'
    matrixfile="cameramatrix.npz"
    CALC=True
    if CALC:
        print("Starting test calculation of camera matrix", myfolder)
        #cameramatrix, distcoeffs = calibrate_camera(myfolder, chessboard=(7,6))
        cameramatrix, distcoeffs = calibrate_camera(myfolder, chessboard=(8,7))
        print("Cameramtx", cameramatrix)
        print("Distcoeffs", distcoeffs)
        save_camera_matrix(myfolder / matrixfile, cameramatrix,distcoeffs)
        # a,b,c,d,e = read_camera_matrix(matrixfile)
        # print("Reading matrix from file")
        # print("Matrix", a)
        # print("Distcoeffs", b)
        from gen_device_config import save_device_camera_matrix
        if cameramatrix is not None
            save_device_camera_matrix(myfolder / "cameramatrix.conf", cameramatrix, distcoeffs, "Generated today")
    else:
        undistort_pic(myfolder / 'left01.jpg', 'myfile.npz' )
