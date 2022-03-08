"gammatest"
from math import sin
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter
from matplotlib import pyplot as plt


def change_contrast(infile, outfile, val):
    # reduse contrast in picture
    img = Image.open(infile)
    enhanger = ImageEnhance.Contrast(img)
    out = enhanger.enhance(val)
    out.save(outfile) 
    return

def change_brightness(infile, outfile, val):
    # reduse contrast in picture
    img = Image.open(infile)
    enhanger = ImageEnhance.Brightness(img)
    out = enhanger.enhance(val)
    out.save(outfile) 
    return

def blur(infile, outfile, val=1):
    # reduse contrast in picture
    img = Image.open(infile)
    blurImage = img.filter(ImageFilter.BLUR)
    blurImage.save(outfile) 
    return


FREQ = 0.23
AMPL = 30
SLOPE = +0.008
OFFSET = -1.9

def testfile(filename):
    print(filename)
    img = Image.open(filename)
    grey = img.convert('L')
    print (grey.format, grey.size, grey.mode)
    col = int(grey.width / 2)
    print (col)

    vallist = []
    for p in range(0,grey.height):
        vallist.append(grey.getpixel((col, p)))
    heigh = grey.height
    maxval = max(vallist)
    minval = min(vallist)
    print (maxval,minval)
    AMPL = (max(vallist[0:22]) - min (vallist[0:22]))/2
    slope = max(vallist[0:30]) - max(vallist[130:160])
    print ("slope", slope)
    yoff = max(vallist[0:30]) - AMPL*2

    sinlist = []
    for i in range(0, heigh):
        ang = 0 + FREQ * i
        sinlist.append ( sin(ang+OFFSET) * AMPL + yoff - slope*(i-180)/180)

    plt.title(str(filename))
    plt.plot(vallist)
    plt.plot(sinlist)
    plt.ylabel('some numbers')
    plt.show()

BASE = Path(__file__).parent
IMAGE=Path(__file__).parent / "0.png"

change_contrast(IMAGE, BASE / 'contrast.jpg', 0.4)
change_brightness(IMAGE, BASE / 'bright.jpg', 0.6)
# blur(IMAGE, BASE / 'blur.jpg', 0.6)
testfile(IMAGE)
#testfile(BASE / 'blur.jpg')
testfile(BASE / 'contrast.jpg')
testfile(BASE / 'bright.jpg')
#testfile(BASE / 'gamma1.jpg')
#testfile(BASE / 'gamma_1.jpg')

