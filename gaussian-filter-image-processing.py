import math
import cv2
import numpy as np


def gaussian_mask(size, sigma):
    gauss_mask = np.zeros((size, size), np.float32)

    for i in range(size):
        for j in range(size):
            norm = math.pow(i - 1, 2) + pow(j - 1, 2)
            gauss_mask[i, j] = math.exp(-norm / (2 * math.pow(sigma, 2))) / 2 * math.pi * pow(sigma, 2)

    return gauss_mask / np.sum(gauss_mask)


def convolution2d(img_gray, mask):
    img_h, img_w = img_gray.shape
    mask_h, mask_w = mask.shape

    for i in range(int(mask_h / 2), img_h - int(mask_h / 2)):
        for j in range(int(mask_h / 2), img_w - int(mask_h / 2)):
            sum = 0
            for k in range(0, mask_h):
                for l in range(0, mask_h):
                    sum += img_gray[i - int(mask_h / 2) + k, j - int(mask_h / 2) + l] * mask[k, l]
            img_gray[i, j] = sum

    return img_gray


# main

img = cv2.imread("image.jpg")
mask = gaussian_mask(size=3, sigma=1.5)

print("Gaussian 3*3 mask : ")
print(mask)

print("\n\nPlease Wait ...")

# split R G B
img_B, img_G, img_R = cv2.split(img)

# save R G B of image
cv2.imwrite("Save Result/1_R G B/image_B.jpg", img_B)
cv2.imwrite("Save Result/1_R G B/image_G.jpg", img_G)
cv2.imwrite("Save Result/1_R G B/image_R.jpg", img_R)

# convolution R G B with Gaussian mask
img_gauss_B = convolution2d(img_B, mask)
img_gauss_G = convolution2d(img_G, mask)
img_gauss_R = convolution2d(img_R, mask)

# save filtered R G B
cv2.imwrite("Save Result/2_image filtered/image_filtered_B.jpg", img_gauss_B)
cv2.imwrite("Save Result/2_image filtered/image_filtered_G.jpg", img_gauss_G)
cv2.imwrite("Save Result/2_image filtered/image_filtered_R.jpg", img_gauss_R)

# merge R G B into one image
img_gauss = cv2.merge([img_gauss_B, img_gauss_G, img_gauss_R])

# save filtered image
cv2.imwrite("Save Result/2_image filtered/image_filtered.jpg", img_gauss)

# down sample original image and save it
img_down_sample = img[::2, ::2, :]
cv2.imwrite("Save Result/1_image_down_sample.jpg", img_down_sample)

# down sample filtered image and save it
img_filtered_down_sample = img_gauss[::2, ::2, :]
cv2.imwrite("Save Result/2_image_filtered_down_sample.jpg", img_filtered_down_sample)

# save both into one image for comparison
img_compare = np.hstack((img_down_sample, img_filtered_down_sample))
cv2.imwrite("Save Result/3_img_compare.jpg", img_compare)

print("Done!")
