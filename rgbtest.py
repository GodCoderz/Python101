import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('rgbtest.png')
# 'img' is 3-D Intensity array - Intensity[X,Y and COLOR]
# COLOR - 'RED' is at index 0, 'GREEN' at index 1, 'BLUE' at 2
# The above assumes RGB format

# extract RGB channels in separate array
r = img[:,:,0] #2D Red   Intensity matrix - [X,Y] 
g = img[:,:,1] #2D Green Intensity matrix - [X,Y] 
b = img[:,:,2] #2D Blue  Intensity matrix - [X,Y] 

img1 = np.array([b,g,r]) 
# The above array has dimensions [COLOR, X, Y]
# So it needs to reshaped to get the desired dimension [X, Y, COLOR]
img1 = np.swapaxes(img1, 0, 1) # [X, COLOR, Y]
img1 = np.swapaxes(img1, 1, 2) # [X, Y, COLOR]

img2 = np.array([0.5*g,0.5*r,0.5*b])
img2 = np.swapaxes(img2, 0, 1)
img2 = np.swapaxes(img2, 1, 2)

cmap = 'gray' #grayscale

plt.figure(figsize=(15,10))

# Tiled subplots
#
plt.subplot(231)
plt.imshow(img, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image in RGB')

#
plt.subplot(232)
plt.imshow(img1, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image in BGR')

#
plt.subplot(233)
plt.imshow(img2, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image (1/2 intensity) GRB')

#
plt.subplot(234)
plt.imshow(r, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Red Channel')
plt.colorbar()

#
plt.subplot(235)
plt.imshow(g, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Green Channel')
plt.colorbar()

#
plt.subplot(236)
plt.imshow(b, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Blue Channel')
plt.colorbar()

plt.show()