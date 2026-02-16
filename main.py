import cv2
from cv2 import *

# cv version
print(cv2.__version__)

# Window name is win for now
cv2.namedWindow("win",0)
cv2.resizeWindow("win",1500,1500)

# read image
img = cv2.imread("test/redwall.jpg")
cv2.imshow("win",img)

while True:
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord('p'):
        print("hello")

cv2.destroyAllWindows()

