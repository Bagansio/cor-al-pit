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



def draw_countours(ds):
    for i, slice in enumerate(ds.pixel_array):
        if i > 5:
            break
        cv2.imshow('Binary image', slice)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        image_gray = cv2.cvtColor(slice, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY)
        cv2.imshow('Binary image', thresh) 
        cv2.waitKey(0)
        #cv2.imwrite('image_thres1.jpg', thresh)
        cv2.destroyAllWindows()
        contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        
        slice_copy = slice
        cv2.drawContours(image=slice_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        cv2.imshow('None approximation', slice_copy)
        cv2.waitKey(0)
        cv2.imwrite(f'images\\contours_none_image{i:03n}.jpg', slice_copy)
        cv2.destroyAllWindows()

    

# MAIN starts here

#path = "DICOM\\1003\\0W\DICOM OK\\2018-04-12-17-52-41.dcm"
path = "DICOM\\1003\\0W\\DICOM OK\\2018-04-12-17-53-27.dcm"
ds = dcmread(path)
#render_video_from_images()
#render_images()
draw_countours(ds)

