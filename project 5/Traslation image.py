

import cv2
import numpy

#image translation extend size of image

image = cv2.imread('test.jpg')
#print height , width type as tuple
print(image.shape,type(image.shape))

height,width =image.shape[:2]
print(height," height")
print(width,' width')

quarter_height,quarter_width = height/4 , width/4

Trans = numpy.float32([[1,0,quarter_width],[0,1,quarter_height]])
print(Trans)
image_trans = cv2.warpAffine(image,Trans,(width,height))
cv2.imshow('image Translation',image_trans)
cv2.waitKey()
cv2.destroyAllWindows()
