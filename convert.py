import numpy as np
import cv2
import numpy as np


from PIL import Image
image = Image.open('javid.png')
 
# summarize some details about the image
image = np.array(image)
image = image[:,:,1]

image[image<=100] = 0
image[image>=200] = 0

im = Image.fromarray(image)
im.save("output.jpeg")

