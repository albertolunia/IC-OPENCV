import cv2
# read image 
image = cv2.imread('84.png')
# show the image, provide window name first
cv2.imshow('image window', image)
# add wait key. window waits until user presses a key
cv2.waitKey(0)
# and finally destroy/close all open windows
cv2.destroyAllWindows()