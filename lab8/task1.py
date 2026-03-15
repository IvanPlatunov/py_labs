import cv2

image = cv2.imread("lab8/variant-3.jpeg")
hsv_im = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # type: ignore
cv2.imshow("HSV image", hsv_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
