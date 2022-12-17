from __future__ import print_function
from pydicom import dcmread
import os
from os.path import isfile, join
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import numpy as np
import cv2

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


def map_dicom():
    fpath = "DICOM"
    for root, dirs, files in walk(fpath):
        for file in files:
            full_path = root+"\\"+file
            print("<------------------------------------->")
            print(f"File path........: {full_path}")
            print("<------------------------------------->")
            ds = dcmread(full_path)
            print(ds)
        #print(root, dirs, files)

def render_images(ds):
    for i, slice in enumerate(ds.pixel_array):
        plt.imshow(slice)
        plt.savefig(f'images\\slice_{i:03n}.png')


def render_video_from_images():
    image_folder = 'images'
    video_name = 'video.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 10, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


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