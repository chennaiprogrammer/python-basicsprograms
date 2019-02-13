

import cv2
#image loads as input
image=cv2.imread('test.jpg')
cv2.imshow('original',image)
cv2.waitKey()
#cvt to color 2 to grayscale

grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('greyimage',grayscale)
cv2.waitKey()
cv2.destroyAllWindows()
