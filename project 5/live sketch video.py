

import cv2

def sketch(image):
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_gray_blur=cv2.GaussianBlur(image_gray,(5,5),0)
    Canny_edges=cv2.Canny(img_gray_blur,10,70)
    rer,mask=cv2.threshold(Canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask
cap = cv2.VideoCapture(0)

while(True):
    ret,frame =cap.read()
    cv2.imshow('live sketch',sketch(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()



