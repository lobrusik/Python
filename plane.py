%cd /
from google.colab import drive
drive.mount('/content/gdrive')

!ln -s /content/gdrive/My\ Drive/ ./mydrive
!ls mydrive

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import skimage, imutils

plane = cv2.imread('/mydrive/samolot_2.jpg')
cv2_imshow(plane)
plane_g=cv2.cvtColor(plane,cv2.COLOR_BGR2GRAY)
res,thresh=cv2.threshold(plane_g, 0, 255, cv2.THRESH_OTSU)
plane_contours = cv2.Canny(plane_g, res -20, res +20)
cv2_imshow(plane_contours)

background = cv2.imread('/mydrive/tlo_grafit.png')
background_g = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
img1 = cv2.resize(plane_contours, (640,480))
img2 = cv2.resize(background_g, (640,480))
Add= cv2.addWeighted(img2, 0.5, img1, 0.5, 0)
cv2_imshow(Add)
