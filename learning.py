from __future__ import print_function
from pydicom import dcmread
import os
from os.path import isfile, join
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from numpy import asarray




### function that returns true if ndim < 4 also tell some errors
# example : If dataset is a video will have 4 dims and then ds.pixel_array will be a matrix
def valid_imshow_data(data):
    data = np.asarray(data)
    if data.ndim == 2:
        return True
    elif data.ndim == 3:
        if 3 <= data.shape[2] <= 4:
            return True
        else:
            print('The "data" has 3 dimensions but the last dimension '
                  'must have a length of 3 (RGB) or 4 (RGBA), not "{}".'
                  ''.format(data.shape[2]))
            return False
    else:
        print('To visualize an image the data must be 2 dimensional or '
              '3 dimensional, not "{}".'
              ''.format(data.ndim))
        return False


# map dicom folder it could be improved to obtain a list of files with path to automatize analisis
def map_dicom():
    fpath = "DICOM"
    for root, dirs, files in os.walk(fpath):
        for file in files:
            full_path = root+"\\"+file
            print("<------------------------------------->")
            print(f"File path........: {full_path}")
            print("<------------------------------------->")
            ds = dcmread(full_path)
            print(ds)
        #print(root, dirs, files)


# from a dataset of 4dim (video) render in images the video as images
def render_images(ds):
    for i, slice in enumerate(ds.pixel_array):
        plt.imshow(slice)
        plt.savefig(f'images\\slice_{i:03n}.png')


#from a set of images render a .avi video
def render_video_from_images():
    image_folder = r'images'
    image_folder = 'images'
    video_name = 'video.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape


    print("creating video")
    video = cv2.VideoWriter(video_name, 0, 10, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    print("releasing video")
    video.release()
    print("done")


def load_images(image_folder):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    return images
import sys
import os.path
from os import path
import argparse

def dir_path(pathName):
    if os.path.isdir(pathName):
        return pathName
    else:
        raise NotADirectoryError(pathName)

parser = argparse.ArgumentParser(
    description='COR AL PIT is a program that given images determine if your heart is healthy or not.',
    epilog="Example of use: python .\main.py -p 'your_path'")

parser.add_argument('-p','--path', type=dir_path, help= "the path with the videos")

def parse():
    return parser.parse_args()

def usage_help():
    return parser.print_help()

def main(path):
    print(path)


if __name__ == '__main__':
    if(len(sys.argv) == 3):
        parse()
        main("XD")

    else: 
        usage_help()
    video.release()


# MAIN starts here

path = "DICOM\\1003\\0W\DICOM OK\\2018-04-12-17-52-41.dcm"
ds = dcmread(path)
render_video_from_images()
#render_images(ds)




"""
for f in onlyfiles:    
    full_path = fpath+f
    print(f"File path........: {full_path}")
    ds = dcmread(full_path)
    print(ds)

    """

"""
ds = dcmread(fpath)

print()
print(f"File path........: {fpath}")
print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
print()

pat_name = ds.PatientName
print(f"Patient's Name...: {pat_name.family_comma_given()}")
print(f"Patient ID.......: {ds.PatientID}")
print(f"Modality.........: {ds.Modality}")
print(f"Study Date.......: {ds.StudyDate}")
print(f"Image size.......: {ds.Rows} x {ds.Columns}")
print(f"Pixel Spacing....: {ds.PixelSpacing}")


print(ds.pixel_array)
"""
