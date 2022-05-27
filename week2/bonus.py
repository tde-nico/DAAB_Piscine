import matplotlib.pyplot as plt
import numpy as np
'''

def	rgba_to_rgb(img):
	new_img = img.copy()
	for y, row in enumerate(img):
		for x, pixel in enumerate(row):
			new_color = [
				((1 - img[y][x][3]) * 1) + (img[y][x][3] * img[y][x][0])
				((1 - img[y][x][3]) * 1) + (img[y][x][3] * img[y][x][1])
				((1 - img[y][x][3]) * 1) + (img[y][x][3] * img[y][x][2])
			]
			new_img[y][x] = new_color
	return new_img

def	apply_filter(img, filtr):
	new_img = img.copy()
	for y, row in enumerate(img):
		for x, pixel in enumerate(row):
			new_img[y][x] = filtr.new_pixel(new_img[y][x])
	return new_img

def rgb_to_hsl(r, g, b):
	max_color = max(r, g, b)
	min_color = min(r, g, b);
	if r == g == b:
		h = 0.0
		s = 0.0
		l = r
	else:
		d = max_color - min_color
		l = (min_color + max_color) / 2
		if l < 0.5:
			s = d / (max_color + min_color)
		else:
			s = d / (2.0 - max_color - min_color)
		if r == max_color:
			h = (g - b) / (max_color - min_color)
		elif g == max_color:
			h = 2.0 + (b - r) / (max_color - min_color)
		else:
			h = 4.0 + (r - g) / (max_color - min_color)
		h /= 6
		if(h < 0):
			h += 1
	return [(h * 360) / 255, s, l]


def hsl_to_rgb(h, s, l):
	if s == 0:
		r = l
		g = l
		b = l
	else:
		if l < 0.5:
			temp2 = l * (1 + s)
		else:
			temp2 = (l + s) - (l * s)
		temp1 = 2 * l - temp2

		tempr = h + 1.0 / 3.0
		if tempr > 1:
			tempr -=1
		tempg = h
		tempb = h - 1.0 / 3.0
		if tempb < 0:
			tempb += 1

		#Red
		if tempr < 1.0 / 6.0:
			r = temp1 + (temp2 - temp1) * 6.0 * tempr
		elif tempr < 0.5:
			r = temp2
		elif tempr < 2.0 / 3.0:
			r = temp1 + (temp2 - temp1) * ((2.0 / 3.0) - tempr) * 6.0
		else:
			r = temp1

		#Green
		if tempg < 1.0 / 6.0:
			g = temp1 + (temp2 - temp1) * 6.0 * tempg
		elif tempg < 0.5:
			g = temp2
		elif tempg < 2.0 / 3.0:
			g = temp1 + (temp2 - temp1) * ((2.0 / 3.0) - tempg) * 6.0
		else:
			g = temp1

		#Blue
		if tempb < 1.0 / 6.0:
			b = temp1 + (temp2 - temp1) * 6.0 * tempb
		elif tempb < 0.5:
			b = temp2
		elif tempb < 2.0 / 3.0:
			b = temp1 + (temp2 - temp1) * ((2.0 / 3.0) - tempb) * 6.0
		else:
			b = temp1

	return [r, g, b]

def saturate_rgb(r, g, b, k):
	h, s, l = rgb_to_hsl(r, g, b)
	if k >= 0:
		gray_factor = s / 255.0
		var_interval = 255 - s
		s = s + k * var_interval * gray_factor
	else:
		var_interval = s
		s = s + k * var_interval
	return hsl_to_rgb(h, s, l)
	


class	Color:
	def __init__(self, R, G, B, A):
		self.r = R
		self.g = G
		self.b = B
		self.a = A

	def get_rgba(self):
		def bound(channel):
			return max(min(channel, 1), 0)
		return [bound(self.r), bound(self.g), bound(self.b), self.a]

	def contrast(self, k):
		return ((self - Color.grey) * k) + Color.grey
	
	def saturate(self, k):
		r, g, b = saturate_rgb(self.r, self.g, self.b, k)
		return Color(r, g, b, self.a)

	def __sub__(self, other):
		return Color(self.r - other.r, self.g - other.g, self.b - other.b, self.a)

	def __mul__(self, k):
		return Color(self.r * k, self.g * k, self.b * k, self.a)

	def __add__(self, other):
		return Color(self.r + other.r, self.g + other.g, self.b + other.b, self.a)

Color.grey = Color(.5, .5, .5, 1)

class	Contrast_Filter:
	def __init__(self, k):
		self._k = k  
	def new_pixel(self, pixel):
		new_pixel = Color(*pixel)
		return new_pixel.contrast(self._k).get_rgba()

class	Saturation_Filter:
	def __init__(self, k):
		self._k = k  
	def new_pixel(self, pixel):
		new_pixel = Color(*pixel)
		return new_pixel.saturate(self._k).get_rgba()

class	Amaro_Filter:
	def __init__(self, hue=0.9, saturation=1.6, contrast=0.8): # other (1.1, 1.5, 0.9)
		self.h = hue
		self.s = saturation
		self.contrast = contrast
	def new_pixel(self, pixel):
		r, g, b, a = pixel
		h, s, l = rgb_to_hsl(r, g, b)
		s = min(s * self.s, 1)
		h = min(h *self.h, 179/255)
		return Color(*hsl_to_rgb(h, s, l), 1).contrast(self.contrast).get_rgba()

class	Nashville_Filter:
	def __init__(self, hue=1, saturation=0.9, contrast=1.4): # other (1.1, 1.5, 0.9)
		self.h = hue
		self.s = saturation
		self.contrast = contrast
	def new_pixel(self, pixel):
		r, g, b, a = pixel
		h, s, l = rgb_to_hsl(r, g, b)
		s = min(s * self.s, 1)
		h = min(h *self.h, 179/255)
		return Color(*hsl_to_rgb(h, s, l), 1).contrast(self.contrast).get_rgba()

#'''
#'''

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
	#img_bright = img_bright.astype(np.uint8)
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
	#rows, cols = img.shape[:2]
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
	#img = vignette(img,247,218,174,0.2)
	return img

def toaster_filter(img, hue=1, saturation=0.9, contrast=1.4, brightness=-20):
	img = replace_color(img,0,0,0,0,0,128,51,0,0)
	img = replace_color(img,150,255,50,170,255,128,51,0,0)
	img = hue_saturation(img, hue, saturation)
	img = brightness_contrast(img, contrast, brightness)
	#img = vignette(img,128,128,128,0.2)
	img = vignette(img,255,99,66,0.1)
	img = vignette(img,250,250,0,0.3)
	return img

im = cv2.imread("42_photo.png")
img = nashville_filter(im)
plt.imshow(img)
plt.show()

#'''
'''

def	toaster(img):
	cb = img if img.mode == 'RGB' else img.convert('RGB')


img = plt.imread("week2/42_photo.png")

#amaro_img = apply_filter(img, Amaro_Filter())
#nashville_img = apply_filter(img, Nashville_Filter())


plt.imshow(img)
plt.show()
#'''
'''

from PIL import Image
import pilgram

im = Image.open("week2/42_photo.png")
img = pilgram.nashville(im)
plt.imshow(img)
plt.show()

#im = Image.open("week2/42_photo.png")
img = pilgram.rise(im)
plt.imshow(img)
plt.show()

#im = Image.open("week2/42_photo.png")
img = pilgram.xpro2(im)
plt.imshow(img)
plt.show()

#im = Image.open("week2/42_photo.png")
img = pilgram.toaster(im)
plt.imshow(img)
plt.show()

#'''