import cv2 as cv
import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("imagensOrganizadas/0.png")
plt.imshow(img)
plt.show()

grey = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
plt.imshow(grey, cmap="gray")
plt.show()

kernel = np.ones((5,5),np.uint8)
# Blurring and erasing little details
grey = cv.GaussianBlur(grey,(9,9),0)
grey = cv.morphologyEx(grey, cv.MORPH_OPEN, kernel)
grey = cv.morphologyEx(grey, cv.MORPH_CLOSE, kernel)
plt.imshow(grey,cmap="gray")
plt.show()

canny = cv.Canny(grey,100,200)
plt.imshow(canny,cmap="gray")
plt.show()

circles = cv.HoughCircles(grey,
                          cv.HOUGH_GRADIENT,
                          dp=1,
                          minDist=20,
                          param1=50,
                          param2=50,
                          minRadius=0,
                          maxRadius=0)
print(circles)

# Changing the dtype  to int
circles = np.uint16(np.around(circles))
cimg = img.copy()
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(cimg, (i[0], i[1]), 2, (255, 0, 0), 10)

plt.imshow(cimg)
plt.show()

"""resize_image = cv2.imread('imagensOrganizadas/0.png', 0)
img = cv2.resize(resize_image, (640, 480))
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30, minRadius=0, maxRadius=30)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('teste', cimg)
cv2.waitKey(0)"""
