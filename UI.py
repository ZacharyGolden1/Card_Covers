import cv2
import numpy as np

# Initialize global variables
drawing = False
top_left_corner = None
bottom_right_corner = None

# Mouse callback function
def draw_square(event, x, y, flags, param):
    global top_left_corner, bottom_right_corner, drawing, sx, sy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left_corner = (x, y)
        sx, sy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        bottom_right_corner = (sx + min(x,y),sy + min(x,y))
        cv2.rectangle(img, top_left_corner, bottom_right_corner, (255, 0, 0), 2)

# Create a black image and a window
img = np.zeros((512, 512, 3), np.uint8) + 255
cv2.namedWindow('Rectangle Drawer')

# Bind the mouse callback function to window
cv2.setMouseCallback('Rectangle Drawer', draw_square)

while True:
    cv2.imshow('Rectangle Drawer', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
