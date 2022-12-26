import os 
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def convert(xmin, w, ymin, h, w_img, h_img):
    xcenter = (xmin + w/2) / w_img
    ycenter = (ymin + h/2) / h_img
    w = w / w_img
    h = h / h_img

    return xcenter, ycenter, w, h


def reverse_convert(xcenter, ycenter, w, h, w_img, h_img):
    h = h * h_img
    w = w * w_img
    x = (xcenter * w_img) - w/2
    y = (ycenter * h_img) - h/2

    return x, y, w + x,  y + h


def yolobbox2bbox(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2



def bbox1(img):
    a = np.where(img != 0)
    bbox = np.min(a[1]), np.max(a[1]), np.min(a[0]), np.max(a[0])
    return bbox

def find_bbox(img:np.array) -> list:
    "find bbox using masks"
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # threshold
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

    # get contour bounding boxes and draw on copy of input
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    bboxes = []
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        bboxes.append([x,y,w,h])
    
    return bboxes
