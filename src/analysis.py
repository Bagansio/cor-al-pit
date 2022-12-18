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
import progressbar
import operator
import time
from cardiac_cycle_algorithm import cardiac_cycle



load_dotenv()
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_EXE')


class DataForm: 
    pass

widgets = [
        '\x1b[33mAnalyzing frames \x1b[39m',
        progressbar.Percentage(),
        progressbar.Bar(marker='\x1b[32m#\x1b[39m'),
    ]

def detect_color(rgb, image, lower_row, max_row, lower_col, max_col, up, right):
    img = image.convert('RGBA')

    pixel_position = []

    #print(max_col)
    #print(max_row)

    if (up):
        for row in range(max_row, lower_row, -1):
            #print(row)
            if (right):
                for col in range(lower_col, max_col):
                    #print(col)
                    pixel = img.getpixel((col, row))
                    #print(pixel)
                    if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                        pixel_position = (col, row)
                        return pixel_position
            if (not right):
                for col in range(max_col, lower_col, -1):
                    #print(col)
                    pixel = img.getpixel((col, row))
                    #print(pixel)
                    if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                        pixel_position = (col, row)
                        return pixel_position
    else:
        for row in range(lower_row, max_row):
            #print(row)
            if (right):
                for col in range(lower_col, max_col):
                    #print(col)
                    pixel = img.getpixel((col, row))
                    #print(pixel)
                    if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                        pixel_position = (col, row)
                        return pixel_position
            if (not right):
                for col in range(max_col, lower_col, -1):
                    #print(col)
                    pixel = img.getpixel((col, row))
                    #print(pixel)
                    if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                        pixel_position = (col, row)
                        return pixel_position            

    return pixel_position

    #for item in data:
        #if item[0] == rgb[0] and item[1] == rgb[1] and item[2] == rgb[2]:
            #return True
    #return False

def detect_external_color(image, upper_internal_wall, rgb, up):
    img = image.convert('RGBA')
    
    first_row = upper_internal_wall[1]
    max_col = upper_internal_wall[0] + 3
    lower_col = upper_internal_wall[0] - 3
    pixel_position = []

    if (up):
        last_row = upper_internal_wall[1] - 150
        for row in range(first_row, last_row, -1):
            for col in range(lower_col, max_col):
                pixel = img.getpixel((col, row))
                if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                    if (check_if_external_wall(img, rgb, row - 1, row - 10, max_col - 1, lower_col + 1, True)):
                        #print("Checking")
                        pixel_position = (col, row)
                        return pixel_position
    else:
        last_row = upper_internal_wall[1] + 150
        for row in range(first_row, last_row):
            for col in range(lower_col, max_col):
                pixel = img.getpixel((col, row))
                if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                    if (check_if_external_wall(img, rgb, row + 1, row + 10, max_col - 1, lower_col + 1, False)):
                        #print("Checking")
                        pixel_position = (col, row)
                        return pixel_position        

    return pixel_position


def check_if_external_wall(img, rgb, actual_row, last_row, max_col, lower_col, up):
    counter = 0
    is_external_wall = False

    if (up):
        for row in range(actual_row, last_row, -1):
            pixel_in_line = False
            for col in range(lower_col, max_col):
                pixel = img.getpixel((col, row))
                if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                    if (not pixel_in_line):
                        counter = counter + 1
                    pixel_in_line = True
    else:
        for row in range(actual_row, last_row):
            pixel_in_line = False
            for col in range(lower_col, max_col):
                pixel = img.getpixel((col, row))
                if (pixel[0] == rgb[0] and pixel[1] == rgb[1] and pixel[2] == rgb[2]):
                    if (not pixel_in_line):
                        counter = counter + 1
                    pixel_in_line = True

    if (counter >= 4):
        is_external_wall = True
    
    return is_external_wall
                



def find_upper_internal_wall(slice_copy_image, rgb, psla):

    if psla:

        pixel_position = detect_color(rgb, slice_copy_image, 280, 335, 650, 700, True, True)
        if (not pixel_position): 
            #print("Yepa")
            pixel_position = detect_color(rgb, slice_copy_image, 280, 335, 600, 650, True, False)

    #else:

    #print(pixel_position)

    return pixel_position

def find_lower_internal_wall(slice_copy_image, rgb, psla):

    if psla:
        pixel_position = detect_color(rgb, slice_copy_image, 500, 550, 650, 700, False, True)
        if (not pixel_position):
            #print("Yepa")
            pixel_position = detect_color(rgb, slice_copy_image, 500, 550, 600, 650, False, False)
    #else:
    
    return pixel_position

def find_upper_external_wall(slice_copy_image, rgb, upper_internal_wall):
    if not upper_internal_wall:
        return None
    upper_internal_wall_list = list(upper_internal_wall)
    upper_internal_wall_list[1] = upper_internal_wall_list[1] - 20
    #print(upper_internal_wall_list)
    pixel_position = detect_external_color(slice_copy_image, upper_internal_wall_list, rgb, True)

    return pixel_position

def find_lower_external_wall(slice_copy_image, rgb, lower_internal_wall):
    if not lower_internal_wall:
        return None
    lower_internal_wall_list = list(lower_internal_wall)
    lower_internal_wall_list[1] = lower_internal_wall_list[1] + 15
    #print(lower_internal_wall_list)
    pixel_position = detect_external_color(slice_copy_image, lower_internal_wall_list, rgb, False)

    return pixel_position

def draw_countours(slice, pixel_spacing, psla, show = False):
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

    if show:
        if psla:
            cv2.line(slice_copy, (650,800), (650,0), (0,255,255), 1) #650,525 650,300
            cv2.line(slice_copy, (600,500), (700,500), (0,255,255), 1)
            cv2.line(slice_copy, (600,335), (700,335), (0,255,255), 1)
            cv2.imshow('None approximation', slice_copy)
            cv2.waitKey(0)
        #else:
    slice_copy_image = Image.fromarray(slice_copy)
    rgb = (0, 255, 0)


    upper_internal_wall = find_upper_internal_wall(slice_copy_image, rgb, psla)
    upper_external_wall = find_upper_external_wall(slice_copy_image, rgb, upper_internal_wall)
    lower_internal_wall = find_lower_internal_wall(slice_copy_image, rgb, psla)
    lower_external_wall = find_lower_external_wall(slice_copy_image, rgb, lower_internal_wall)
    """
    print(upper_internal_wall)
    print(upper_external_wall)
    print(lower_internal_wall)
    print(lower_external_wall)
    """
    if show:

        if psla:
            cv2.line(slice_copy, (0,0), upper_internal_wall, (0,255,255), 1)
            cv2.line(slice_copy, (0,0), lower_internal_wall, (0,255,255), 1)
            cv2.line(slice_copy, (0,0), upper_external_wall, (0,0,255), 1)
            cv2.line(slice_copy, (0,0), lower_external_wall, (0,0,255), 1)
            cv2.imshow('None approximation', slice_copy)
            cv2.waitKey(0)
        #else:

    result = DataForm()

    if not upper_internal_wall or not upper_external_wall or not lower_internal_wall or not lower_external_wall:
        result.top = None
        result.mid = None
        result.bot = None
    else:
        result.top = abs(upper_internal_wall[1] - upper_external_wall[1]) * pixel_spacing[1]
        result.mid = abs(lower_internal_wall[1] - upper_internal_wall[1]) * pixel_spacing[1]
        result.bot = abs(lower_internal_wall[1] - lower_external_wall[1]) * pixel_spacing[1]


    #print(result.__dict__)

    return result


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
    

def analyze_video(path, psla = True):
    ds = dcmread(path)
    pixel_spacing = ds.PixelSpacing # [0] x separation between pixels, [1] y separation
    
    bar = progressbar.ProgressBar(widgets=widgets, max_value=len(ds.pixel_array)).start()

    data_arrays = DataForm()
    heart_rate_array = []
    data_arrays.top = []
    data_arrays.mid = []
    data_arrays.bot = []
    for i, slice in enumerate(ds.pixel_array):

        if i % 20 == 0:
            hr = get_heart_rate(slice)
            if hr is not None:
             heart_rate_array.append(hr)

        result = draw_countours(slice,pixel_spacing,psla)
        data_arrays.top.append(result.top)
        data_arrays.mid.append(result.mid)
        data_arrays.bot.append(result.bot)
        bar.update(i + 1)

    bar.finish()
    # call to function
    data = cardiac_cycle(data_arrays) 
    if len(heart_rate_array) > 0:
        data.hr = numpy.mean(heart_rate_array)

    print(data.__dict__, len(data_arrays.top))
    return data

#video = "DICOM\\1003\\0W\\DICOM OK\\2018-04-12-17-53-27.dcm"
#ds = dcmread(video)
#analyze_video(video)


