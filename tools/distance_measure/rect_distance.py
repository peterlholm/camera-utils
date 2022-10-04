"calculate distance to object given FOV etc"
from pathlib import Path
from math import tan, pi
from find_rectangle import find_rectangle, zoom
import cv2

    FOV = 48    # grader
    FOV_80 = 39 # 0.8 zoom
    OBJ_DIST =1.8

def rect2dist(rectsize, imgheight):
    "calculate distance from 1cm square"
    #print(rectsize, imgheight)
    imgsize = imgheight/rectsize *10 # mm
    height = imgsize/2 /tan(FOV/180*pi/2) - OBJ_DIST   # mm
    return height   # in mm

if __name__ == "__main__":
    myfolder = Path(__file__).parent / 'testimages' / 'distance'
    picture = myfolder / 'picture4.jpeg'
    img = cv2.imread(str(picture))
    img2 = zoom(img, 20)
    rect_size = find_rectangle(img)
    if rect_size is None:
        print("kunne ikke finde rectangle")
    else:
        height = rect2dist(rect_size, img.shape[0])
        print(f'Højden er {height} mm')
 