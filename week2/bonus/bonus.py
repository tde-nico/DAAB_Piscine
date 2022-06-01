'''
# download img
import requests

url = "https://github.com/jelenamikan/opencv-project/blob/master/flowers.jpg?raw=true"
res = requests.get(url)
content = res.content
with open("flowers.jpg", "wb") as f:
	f.write(content)
'''
# you need to download the image

import matplotlib.pyplot as plt
import numpy as np
import cv2

def	hue_saturation(img_rgb, alpha=1, beta=1):
	img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
	hue = img_hsv[:,:,0]
	saturation = img_hsv[:,:,1]
	hue = np.clip(hue * alpha, 0, 179)
	saturation = np.clip(saturation * beta, 0, 255)
	img_hsv[:,:,0] = hue
	img_hsv[:,:,1] = saturation
	return cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

def	brightness_contrast(img, alpha=1.0, beta=0):
	img_contrast = img * (alpha)
	img_bright = img_contrast + (beta)
	img_bright = np.clip(img_bright, 0, 255)
	img_bright = img_bright.astype(np.uint8)
	return img_bright

def	grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def	vignette(img, r, g, b, a):
	color = img.copy()
	color[:,:,0] = b
	color[:,:,1] = g
	color[:,:,2] = r
	return cv2.addWeighted(img, 1-a, color, a, 0)

def replace_color(img, hl=0, sl=0, vl=0, hu=0, su=0, vu=0, nred=0, ngreen=0, nblue=0):
	rows, cols = img.shape[:2]
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower = np.array([hl, sl, vl])
	upper = np.array([hu, su, vu])
	color = cv2.inRange(hsv, lower, upper)
	img[color>0] = (nblue, ngreen, nred)
	return img



def	amaro_filter(img, hue=1.1, saturation=1.5, contrast=0.9, brightness=10):
	img = hue_saturation(img, hue, saturation)
	img = brightness_contrast(img, contrast, brightness)
	return img

def	nashville_filter(img, hue=1, saturation=1.5, contrast=1.2, brightness=10):
	img = hue_saturation(img, hue, saturation)
	img = brightness_contrast(img, contrast, brightness)
	img = replace_color(img,0,0,0,0,0,30,34,43,109)
	img = replace_color(img,0,0,200,0,0,255,247,218,174)
	img = vignette(img,247,218,174,0.2)
	return img

def toaster_filter(img, hue=1, saturation=0.9, contrast=1.4, brightness=-20):
	img = replace_color(img,0,0,0,0,0,128,51,0,0)
	img = replace_color(img,150,255,50,170,255,128,51,0,0)
	img = hue_saturation(img, hue, saturation)
	img = brightness_contrast(img, contrast, brightness)
	img = vignette(img,128,128,128,0.2)
	img = vignette(img,255,99,66,0.1)
	img = vignette(img,250,250,0,0.3)
	return img

def hudson_filter(img, hue=1, saturation=1.1, contrast=0.9, brightness=40):
	img = hue_saturation(img, hue, saturation)
	img = brightness_contrast(img, contrast, brightness)
	return img

# original
im = cv2.imread("/content/flowers.jpg")
plt.imshow(im[:,:,::-1])
plt.show()
# amaro
im = cv2.imread("/content/flowers.jpg")
img = amaro_filter(im)
plt.imshow(img[:,:,::-1])
plt.show()
# nashville
im = cv2.imread("/content/flowers.jpg")
img = nashville_filter(im)
plt.imshow(img[:,:,::-1])
plt.show()
# toaster
im = cv2.imread("/content/flowers.jpg")
img = toaster_filter(im)
plt.imshow(img[:,:,::-1])
plt.show()
# hudson
im = cv2.imread("/content/flowers.jpg")
img = hudson_filter(im)
plt.imshow(img[:,:,::-1])
plt.show()
