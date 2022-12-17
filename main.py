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
        plt.savefig(f'C:\\Users\\farri\\OneDrive\\Escriptori\\Hackaton\\images\\slice_{i:03n}.png')


#from a set of images render a .avi video
def render_video_from_images():
    image_folder = r'C:\Users\farri\OneDrive\Escriptori\Hackaton\images'
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

#Should be included in new class
def draw_contours():
    image_folder = r'C:\Users\farri\OneDrive\Escriptori\Hackaton\images'
    images = load_images(image_folder);

    print("images loaded")

    #image = images[0]

    image = Image.open(image_folder + "\\slice_001.png" )

    print(image.format)
    print(image.size)
    print(image.mode)

    cv2.imshow('Binary image', asarray(image))
    cv2.waitKey(0)

    image_gray = cv2.cvtColor(asarray(image), cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(image_gray, 75, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary image', thresh) 
    cv2.waitKey(0)
    cv2.imwrite('image_thres1.jpg', thresh)
    cv2.destroyAllWindows()



    

# MAIN starts here

#path = "DICOM\\1003\\0W\DICOM OK\\2018-04-12-17-52-41.dcm"
path = "C:\\Users\\farri\\OneDrive\\Escriptori\\Hackaton\\HACKATHON VIDEOS COR 2022\\HACKATHON VIDEOS COR 2022\\DICOM\\1003\\0W\\DICOM OK\\2018-04-12-17-53-27.dcm"
ds = dcmread(path)
#render_video_from_images()
#render_images(ds)
draw_contours()




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