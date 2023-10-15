import numpy as np
import imageio.v2
import scipy.ndimage
import cv2

img ="D:\SYSTEM DATA\Documents\GAYATHRI\IMGPROJECT\Halle_Berry.png"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

def sketchify(front,back):
    sketch=front*255/(255-back)
    sketch[sketch>255]=255
    sketch[back==255]=255
    return sketch.astype('uint8')

imgread=imageio.imread(img)
gray=rgb2gray(imgread)

i=255-gray
dim=scipy.ndimage.filters.gaussian_filter(i,sigma=25)

imgsketch=sketchify(dim,gray)
cv2.imwrite('HalleBerrysketches.png',imgsketch)