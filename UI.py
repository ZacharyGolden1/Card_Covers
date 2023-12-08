import cv2
import numpy as np

# Initialize global variables
drawing = False
top_left_corner = None
bottom_right_corner = None

# Mouse callback function
def draw_square(event, x, y, flags, param):
    global top_left_corner, bottom_right_corner, drawing, x1, y1

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left_corner = (x, y)
        x1, y1 = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        dist = int(np.sqrt((x-x1)**2 + (y-y1)**2) / np.sqrt(2))
        x2, y2 = x1 + dist, y1 + dist
        bottom_right_corner = (x2,y2)
        cv2.rectangle(img, top_left_corner, bottom_right_corner, (255, 0, 0), 2)
        c = ((x1 + x2)//2,(y1 + y2)//2)
        r = int(np.sqrt((x2-x1)**2)/2)
        cv2.circle(img, c, r, color=(255, 0, 0), thickness=2)

# Create a white image and a window
img = np.zeros((512, 512, 3), np.uint8) + 255
cv2.namedWindow('Rectangle Drawer')

# Bind the mouse callback function to window
cv2.setMouseCallback('Rectangle Drawer', draw_square)

while True:
    cv2.imshow('Rectangle Drawer', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
