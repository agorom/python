from PIL import Image

#open the image

image = Image.open("MYPASSPORT.JPG")
#print out the image

#image.show()

#maniplating image
"""
image2 = image.resize((10, 5))
image2.save("resize_image.jpg")
"""

image3 = image.convert("PNG")
image3.save("leo.png")

image3.show()