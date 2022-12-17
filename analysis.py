from __future__ import print_function
from pydicom import dcmread
import os
from os.path import isfile, join
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import numpy
import cv2
from PIL import Image
from numpy import asarray
import pytesseract
from itertools import chain
from dotenv import load_dotenv
import operator


load_dotenv()
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_EXE')


class DataForm: 
    pass

def detect_color(rgb, image, lower_row, max_row, lower_col, max_col):
    img = image.convert('RGBA')
    data = img.getdata()

    pixel_position = []
    found = False

    print(max_col)
    print(max_row)

    for row in range((max_row, lower_row, -1) and not found):
        print(row)
        for col in range((lower_col, max_col) and not found):
            print(col)
            pixel = img.getpixel((col, row))
            print(pixel)
            if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                found = True
                pixel_position = (row, col)

    return pixel_position

    #for item in data:
        #if item[0] == rgb[0] and item[1] == rgb[1] and item[2] == rgb[2]:
            #return True
    #return False


def find_upper_internal_wall(slice_copy_image):
    found = False
    rgb = (0, 255, 0)
    pixel_position = detect_color(rgb, slice_copy_image, 280, 335, 525, 575)
    if (not pixel_position): 
        print("Yepa")
        detect_color(rgb, slice_copy_image, 280, 335, 475, 525)

    print(pixel_position)

    return pixel_position

def draw_countours(slice):
    #cv2.imshow('Binary image', slice)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_gray = cv2.cvtColor(slice, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
    #cv2.imshow('Binary image', thresh) 
    #cv2.waitKey(0)
    #cv2.imwrite('image_thres1.jpg', thresh)
    cv2.destroyAllWindows()
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    
    slice_copy = slice
    cv2.drawContours(image=slice_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    #cv2.imshow('None approximation', slice_copy)
    #cv2.waitKey(0)
    #cv2.imwrite(f'images\\contours_none_image{i:03n}.jpg', slice_copy)
    cv2.destroyAllWindows()
        
    cv2.line(slice_copy, (650,800), (650,0), (0,255,255), 1) #650,525 650,300
    cv2.line(slice_copy, (600,525), (700,525), (0,255,255), 1)
    cv2.line(slice_copy, (600,335), (700,335), (0,255,255), 1)
    cv2.imshow('None approximation', slice_copy)
    cv2.waitKey(0)

    slice_copy_image = Image.fromarray(slice_copy)


    upper_internal_wall = find_upper_internal_wall(slice_copy_image);
    upper_external_wall = (-1, -1);
    lower_internal_wall = (-1, -1);
    lower_external_wall = (-1, -1);



    upper_box = (550, 200, 750, 350)
    lower_box = (550, 475, 750, 625)
    upper_slice_crop = slice_copy_image.crop(upper_box)
    lower_slice_crop = slice_copy_image.crop(lower_box)

    height = slice_copy_image.height
    width = slice_copy_image.width
    print(height)
    print(width)



    #cv2.imshow('None approximation', asarray(upper_slice_crop))
    #cv2.waitKey(0)
    #cv2.imshow('None approximation', asarray(lower_slice_crop))
    #cv2.waitKey(0)    


def get_heart_rate(img):
    # Read image from which text needs to be extracted

    
    # Preprocessing the image starts
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    
    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    
    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)
    
    # Creating a copy of image
    im2 = img.copy()
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
            
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        hr = get_variable_from_text(text, "BPM")
        
        return hr

        


def get_variable_from_text(text, variable, separator="\n"):
    filtered_text = text.split(separator)
    try:
        return int([s for s in filtered_text if variable in s][0].split(variable)[0])
    except Exception:
        return None
    

def analyze_video(path):
    ds = dcmread(path)
    data = DataForm()
    heart_rate_array = []
    for i, slice in enumerate(ds.pixel_array):
        if i % 20 == 0:
            heart_rate_array.append(get_heart_rate(slice))
        if i < 5:
            draw_countours(slice)
    data.hr = numpy.mean(heart_rate_array)

    print(data.__dict__)


analyze_video("DICOM\\1003\\0W\\DICOM OK\\2018-04-12-17-53-27.dcm")


