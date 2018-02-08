"""
@author: Ida Bagus Dwi Satria Kusuma - @dskusuma
"""
import numpy as np
import cv2

# Read color image
img = cv2.imread('gambar1.jpg')

# Get the image height, width, channel
height,width,channel = img.shape

# Create blank CMY image
img_cmyk = np.zeros((height,width,3))

# Create blank CMYK image
#img_cmyk = np.zeros((height,width,4))

#CALCULATE
for i in np.arange(height):
    for j in np.arange(width):
        r = img.item(i,j,0)
        g = img.item(i,j,1)
        b = img.item(i,j,2)
        
        # RGB to CMY
        c = 1 - (r/255.)
        m = 1 - (g/255.)
        y = 1 - (b/255.)
        
        # CMY to CMYK
#        var_K = 1
#        if (c < var_K): var_K = c
#        if (m < var_K): var_K = m
#        if (y < var_K): var_K = y
#        if (var_K == 1):
#            c = 0
#            m = 0
#            y = 0
#        else:
#            c = (c - var_K) / (1.-var_K)
#            m = (m - var_K) / (1.-var_K)
#            y = (y - var_K) / (1.-var_K)
#        
#        K = var_K
        
        img_cmyk.itemset((i,j,0),int(c*100))
        img_cmyk.itemset((i,j,1),int(m*100))
        img_cmyk.itemset((i,j,2),int(y*100))
        # write K to image
#        img_cmyk.itemset((i,j,3),K)

# Write image        
cv2.imwrite('image_cmyk.jpg',img_cmyk)
# View Image
cv2.imshow('image',img_cmyk)
cv2.waitKey(0)
cv2.destroyAllWindows()
