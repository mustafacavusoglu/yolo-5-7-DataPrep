import os 
import cv2
import numpy as np
import pandas as pd


def convert_2(xmin, w_img, ymin, h_img, w, h):
    xcenter = (xmin + w/2) / w_img
    ycenter = (ymin + h/2) / h_img
    w = w / w_img
    h = h / h_img

    return xcenter, ycenter, w, h


def yolobbox2bbox(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2



def bbox1(img):
    a = np.where(img != 0)
    bbox = np.min(a[1]), np.max(a[1]), np.min(a[0]), np.max(a[0])
    return bbox


for i in images:
    img = cv2.imread(i)
    xmin, xmax, ymin, ymax = bbox1(img)
    x, y, w, h = convert(img.shape, (xmin, xmax, ymin, ymax))
    print(x, y, w, h)
    txt_path = i.replace('masks', 'images').replace('.png', '.txt')
    with open(txt_path, 'w') as txt:
        txt.write('0 ' + str(x) + ' ' + str(y) + ' ' +  str(w) + ' ' +  str(h))

