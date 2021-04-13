#install open cv --> type in terminal
#py -3.9 -m pip install opencv-python

import cv2
im_g=cv2.imread("numpy/smallgray.png",0)
#im_c=cv2.imread("numpy/smallgray.png",1) --> to read rgb colour
#print(im_g)

#create pic
cv2.imwrite("numpy/nyotgray.png",im_g)
print(im_g)