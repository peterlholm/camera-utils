#!/bin/python3
import os
from pathlib import Path
from PIL import Image


COLORPICTURE = "image8.jpg"
BLACKWHITEPICTURE = "image8.jpg"
DIASPICTURE = "image0.jpg"
NOLIGHT = "image9.jpg"

OUTCOLOR = "color.png"
OUTDIAS = "dias.png"
OUTNOLIGHT = "nolight.png"

def convert_from_blender(infolder, outfolder):
    pic = Image.open(infolder / COLORPICTURE)
    pic.save(Path(outfolder) / OUTCOLOR)
    pic = Image.open(infolder / DIASPICTURE)
    pic.save(Path(outfolder) / OUTDIAS)
    pic = Image.open(infolder / NOLIGHT)
    pic.save(Path(outfolder) / OUTNOLIGHT)
    return

def traverse_folder(intree, outtree):
    print("Converting Blender folder " + str(intree) + " to " + str(outtree))
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
        if Path.exists(indir):
            outdir = Path(outtree) / str(no)
            os.makedirs(outdir)
            convert_from_blender(indir, outdir)
        else:
            break
        no += 1
        if no % 10 == 0:
            print(".", end='')
    print("")
    return


infolder = Path('testdata/danwand/beige_toothset/210907')
infolder = Path('/home/danbots/TestData/DanWand/beige_toothset/210907/')
outfolder = Path('tmp')
#export_from_blender(infolder,outfolder)

traverse_folder(infolder, outfolder)
