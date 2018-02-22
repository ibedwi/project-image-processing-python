"""
@author : Ida Bagus Dwi Satria Kusuma - @dskusuma
Notes   :
There are two kind of solutions. The first is solution using the Open-CV's
library. The second is without the library.
"""

import numpy as np 
import cv2

# Read color image
img = cv2.imread('gambar1.jpg')

# Get the image's height, width, and channels
height, width, channels = img.shape

# Create blank Binary Image
img_binary = np.zeros((height,width,1))

# Create grayscale image
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print img_grayscale.shape
# ======================================================
# IMPLEMENTATION USING OPENCV LIBRARY 
# ======================================================
# (thresh, img_binary) = cv2.threshold(img_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# ======================================================
# IMPLEMENTATION WITHOUT OPENCV LIBRARY 
# ======================================================
# Set Threshold
thresh = 120
# CALCULATE
for i in np.arange(height):
    for j in np.arange(width):
        x = img_grayscale.item(i,j)
        if x >= thresh:
            y = 1
        else :
            y = 0

        img_binary.itemset((i,j,0),int(y))

# Write image
cv2.imwrite('image_binary.jpg',img_binary)
# View image
cv2.imshow('image',img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()