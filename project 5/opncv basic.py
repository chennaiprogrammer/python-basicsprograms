
import cv2
import numpy

input=cv2.imread('test.jpg')

print(input.shape)

print('height of image',int(input.shape[0]))
print('width of image',int(input.shape[1]))


cv2.imwrite('output.png',input)