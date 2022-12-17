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

# 