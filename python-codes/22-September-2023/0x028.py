import cv2

# load the image
image = cv2.imread("MYPASSPORT.JPG")

# show the image

cv2.imshow("image", image)
cv2.waitkey(0)
cv2.destroyAllwindows()