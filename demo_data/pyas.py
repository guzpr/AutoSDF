import cv2
import numpy as np

# Load the image
image_path = 'anggada256mask.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to isolate the mask
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# Find contours of the mask
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming the largest contour is the mask
mask_contour = max(contours, key=cv2.contourArea)

# Get bounding box coordinates from the contour
x, y, w, h = cv2.boundingRect(mask_contour)

# Draw the bounding box on the original image (optional)
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save or display the image with the bounding box
cv2.imwrite('image_with_bbox.jpg', image)
# cv2.imshow('Image with Bounding Box', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# The bounding box coordinates
bbox = (x, y, x + w, y + h)
print("Bounding box coordinates:", bbox)
