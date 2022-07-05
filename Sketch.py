import cv2

# code in comments can be used for showing
# tranformation of image in each step.
image = cv2.imread("dog.jpg")                            # Reads image using their address
# cv2.imshow("Dog", image)                                 # shows the actual image
# cv2.waitKey(0)                                           # wait for any key to be pressed 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     # converts image to grey
# cv2.imshow("New Dog", gray_image)
# cv2.waitKey(0)
inverted_image = 255 - gray_image
# cv2.imshow("Inverted", inverted_image)
# cv2.waitKey()
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
# cv2.imshow("Sketch", pencil_sketch)
# cv2.waitKey(0)
cv2.imshow("original Dog", image)
cv2.waitKey(0)
cv2.imshow("pencil Dog", pencil_sketch)
cv2.waitKey(0)