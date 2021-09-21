#!/bin/python3
import os
from pathlib import Path
from PIL import Image
#from traverse import traverse_serie

# blender names
COLORPICTURE = "image0.png"
BLACKWHITEPICTURE = "image8.png"
DIASPICTURE = "image0.png"
NOLIGHT = "image9.png"

OUTCOLOR = "color.png"
OUTDIAS = "dias.png"
OUTNOLIGHT = "nolight.png"

def convert_to_blender(infolder, outfolder):
    pic = Image.open(infolder / OUTCOLOR)
    pic.save(Path(outfolder) / COLORPICTURE)
    pic.convert('1')
    pic.save(Path(outfolder) / BLACKWHITEPICTURE)
    pic = Image.open(infolder / OUTDIAS)
    pic.save(Path(outfolder) / DIASPICTURE)
    pic = Image.open(infolder / OUTNOLIGHT)
    pic.save(Path(outfolder) / NOLIGHT)
    return

def export_to_nn(intree, outtree):
    print("Converting folder " + str(intree) + " to nn folder: " + str(outtree))
    if not intree.exists():
        print("No input folder")
        return False
    if outtree.exists():
        print("Output folder exist allready")
        return False
    os.makedirs(outtree) 
    no = 0
    while True:
        indir = intree / str(no)
        if indir.exists():
            outdir = Path(outtree) / ("render" + str(no))
            os.makedirs(outdir)
            convert_to_blender(indir, outdir)
        else:
            #print ("path does not exist", str(indir))
            break
        no += 1
        if no % 10 == 0:
            print(".", end='')
    print("")
    return

infolder = Path('testdata\\original')
outfolder = Path('tmp')

export_to_nn(infolder, outfolder)
