import cv2
import numpy as np

img = cv2.imread('girl.png')

rows,cols = img.shape[0:2]


m45 = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.5) 
print m45
m90 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1.5) 
print m90

r45 = cv2.warpAffine(img, m45,(cols, rows))
r90 = cv2.warpAffine(img, m90,(cols, rows))


cv2.imshow("origin", img)
cv2.imshow("45", r45)
cv2.imshow("90", r90)
cv2.waitKey(0)
cv2.destroyAllWindows()

