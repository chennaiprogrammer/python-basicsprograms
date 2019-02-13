
import cv2
import numpy
image=cv2.imread('images.png')
#method 1
#rotation=cv2.transpose(image)
#cv2.imshow('rotation_image',rotation)

#method 2
height , width = image.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((height/2,width/2),90,1)
rotation_image=cv2.warpAffine(image,rotation_matrix,(height,width))
cv2.imshow('image rotation',rotation_image)
cv2.waitKey()
cv2.destroyAllWindows()





