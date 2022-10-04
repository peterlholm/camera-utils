"Find rectangles in image"
from statistics import mean, stdev
from pathlib import Path
import cv2

_DEBUG = False

def zoom(img, scale=20):
    "scale in procent"
    dim = (int(img.shape[1] * scale / 100), int(img.shape[0] * scale / 100))
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def img_filter(image):
    "filter image"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,151,9)
    #blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    #thresh2 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,151,9)
    #canny = cv2.Canny(thresh, 120, 255, 1)
    return thresh

def find_rect(img):
    "input must be binary"
    min_percent = 15    # persent
    max_square_dif = 15 # persent
    max_stdev = 0.1
    max_area = img.shape[0] * img.shape[1]
    min_area = max_area * min_percent / 100
    rectangles = []
    #contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if _DEBUG:
        print("number contours", len(contours))
    for contour in contours:
        area = cv2.contourArea(contour)
        (x,y,w,h) = cv2.boundingRect(contour)
        if area < min_area:
            if _DEBUG:
                print(f"dropping - to small: {area} ({100*area/max_area:.1f}%) pos {x}, {y} Width {w}, {h}")
        else:
            rect = cv2.minAreaRect(contour)
            #check square
            size = rect[1]
            if abs(size[0]-size[1])/size[0]>max_square_dif/100:
                print(f"this is not a square: {rect}")
            else:
                rectangles.append(rect)
                if _DEBUG:
                    print(f"Rect (center, size, angle) {rect}, Area {area}")
                #box = cv2.boxPoints(rect)
    if _DEBUG:
        print("Rectangles", rectangles)
    sizes = []
    for rect in rectangles:
        sizes.append(rect[1][0])
        sizes.append(rect[1][1])
    if len(sizes)==0:
        return None
    if _DEBUG:
        print("Sizes", sizes)
        print("Mean", mean(sizes))
        print("Stdev", stdev(sizes))
        print(stdev(sizes)/img.shape[0])
    if stdev(sizes)/img.shape[0]>max_stdev:
        print("stdev er for stor")
        print(sizes)
        print(mean(sizes))
        print(stdev(sizes))
        return None
    return mean(sizes)

def find_rectangle(imag):
    #img1 = cv2.imread(str(file))
    #img2 = zoom(img1, 20)
    imag3 = img_filter(imag)
    return find_rect(imag3)

if __name__ == "__main__":
    myfolder = Path(__file__).parent / 'testimages' / 'distance'
    file = myfolder / 'picture4.jpeg'
    img1 = cv2.imread(str(file))
    img2 = zoom(img1, 20)
    img3 = img_filter(img2)
    squaresize = find_rect(img3)
    print("rectangle size",squaresize)
 