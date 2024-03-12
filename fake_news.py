#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 01:05:07 2023

@author: fibonacci
"""


import cv2 as cv
import os

folder_path='/home/fibonacci/Documents/image_classification/car'
if not os.path.exists(folder_path):
    print(f"Error:folder {folder_path} does not exist") 
    
image_files=[f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]


image_path=os.path.join(folder_path,image_files[6])
img=cv.imread(image_path)
if img is not None:
    cv.imshow('Image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print(f"Error: Unable to read image '{image_path}'.")