# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:30:51 2022

@author: user
"""

import os
import cv2
import glob
import logging
import numpy as np
import matplotlib.pyplot as plt


def image_resize(local_path, resize_dim, interpolation=cv2.INTER_AREA, grayscale=False, save=False, save_dir=None):
    """
    params:
        local_path: a folder that contains images.
        resize_dim: dimension of the image.
        grayscale: convert image to 8 bit grayscale.
    """

    try:
        for images in os.listdir(local_path):
            img = cv2.imread(os.path.join(local_path, images))
            img = cv2.resize(img, resize_dim, interpolation=interpolation)
            
            if grayscale:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
            if save:
                cv2.imwrite(os.path.join(save_dir, images),img)
                
        logging.info('Resizing completed!')
        return img
    except TypeError:
        logging.error('Invalid given data')
        return None
    
def binarize(image_path, ext, thresh, maxval, binary, save=False, save_dir=None):
   
    try:
        os.chdir(image_path)
        for image in glob.glob('*.' + ext):
            img = cv2.imread(os.path.join(image_path, image))
            img = cv2.threshold(img, thresh, maxval, binary)
            
            if save:
                cv2.imwrite(os.path.join(save_dir, image),img)
        
        logging.info('Binarize successfully!')
        return img
    except TypeError:
        logging.error('Invalid given data')
        return None
        
def noise_reduction(image_path, ext, gray=False, output=None, h=2, hcolor=2, templateWindowSize=7, searchWindowSize=21):
    """
    params:
        gray : grayscale image
        output : output array
        h : filter strength. Higher h value removes noise better, but removes details of image also
    """
    
    try:
        os.chdir(image_path)
        for image in glob.glob('*.' + ext):
            img = cv2.imread(os.path.join(image_path, image))
            if gray:
                return cv2.fastNlMeansDenoising(img, output, h, templateWindowSize, searchWindowSize)
            else:
                return cv2.fastNlMeansDenoisingColored(img, output, h, hcolor, templateWindowSize, searchWindowSize)
    except TypeError:
        logging.error('Invalid gievn data')
        
def crop_image(image, dim=(64,128)):
    (h, w) = image.shape
    
    if h > dim[0]:
        image = image[:dim[0], :]
    
    if w > dim[1]:
        image = image[:, :dim[1]]
    
    # create white blank image
    new_img = np.ones(dim)*255 
    # fill the array to new image
    new_img[:h, :w] = image 
    
    return new_img