# gaussian-filter-image-processing
This is a Python code that performs Gaussian blurring on an input image using a 2D convolution with a Gaussian kernel. The blurred image is then downsampled and saved along with the original downsampled image for comparison.

The code begins by importing the required libraries - math, cv2, and numpy.

Next, the function gaussian_mask is defined, which takes in two parameters - size and sigma - and returns a 2D numpy array that represents the Gaussian kernel. The function calculates the Gaussian values for each pixel in the kernel based on its distance from the center pixel and the value of sigma. The resulting kernel is then normalized to ensure that the sum of all values in the kernel equals 1.

The function convolution2d is also defined, which performs a 2D convolution between an input grayscale image and a given kernel. The function iterates over each pixel in the image and performs a convolution by multiplying the kernel with the corresponding pixels in the image and summing the resulting values.

The main part of the code begins by loading the input image using the cv2.imread function and storing it in the variable img.

The gaussian_mask function is then called to generate a 3x3 Gaussian kernel with sigma=1.5. This kernel is printed to the console for reference.

Next, the input image is split into its red, green, and blue channels using the cv2.split function. The resulting grayscale images are stored in the variables img_B, img_G, and img_R.

The original R, G, and B channels of the input image are saved to disk using the cv2.imwrite function.

The convolution2d function is then called to perform Gaussian blurring on each of the R, G, and B channels separately using the generated Gaussian kernel. The resulting blurred images are stored in the variables img_gauss_B, img_gauss_G, and img_gauss_R.

The blurred R, G, and B channels are saved to disk using the cv2.imwrite function.

The blurred R, G, and B channels are then merged back into a single color image using the cv2.merge function and stored in the variable img_gauss.

The resulting blurred color image is saved to disk using the cv2.imwrite function.

The input image is then downsampled by a factor of 2 in both dimensions using numpy slicing and saved to disk.

The blurred color image is also downsampled by a factor of 2 in both dimensions using numpy slicing and saved to disk.

Both the original and blurred downsampled images are concatenated horizontally using the numpy function np.hstack and saved to disk for comparison.

Finally, the code prints "Done!" to the console to indicate that the program has completed.
