from skimage.filters import gaussian
from skimage.io import imread, imshow

image = imread("MYPASSPORT.JPG")

smooth_image = gaussian(image, sigma=3)

imshow(smooth_image)
