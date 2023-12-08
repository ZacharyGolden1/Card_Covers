import cv2
import numpy as np
import math

# Initialize global variables
drawing = False
top_left_corner = None
bottom_right_corner = None

def draw_circles(img, c, r, x1, y1, x2, y2):
    # draw center circle in the middle of the image
    cv2.circle(img, c, r, color=(255, 0, 0), thickness=2)

    # initially we draw 4 circles since there are 4 areas in the square that
    # have gaps: UR, DR, DL, UL
    a = np.array([c[0] + r*math.cos(np.pi/4),c[1] - r*math.sin(np.pi/4)])
    b = np.array([x2, y1])
    m = np.linalg.norm(b-a)
    M = np.linalg.norm(b-c)
    n = (m**2)/M
    r = int((m - n)/2)
    c1 = (int((a[0] + (b[0]-n/np.sqrt(2)))/2),
          int((a[1] + (b[1]+n/np.sqrt(2)))/2))
    # import pdb;pdb.set_trace()
    cv2.circle(img, c1, r, color=(255, 0, 0), thickness=2)

    ## DEBUG
    # draw a point at a
    cv2.circle(img, (int(a[0]),int(a[1])), 2, color=(0, 255, 0), thickness=2)
    # draw a point at b
    cv2.circle(img, (int(b[0]),int(b[1])), 2, color=(0, 255, 0), thickness=2)
    # draw a point at c1
    cv2.circle(img, (int(c1[0]),int(c1[1])), 2, color=(0, 255, 0), thickness=2)
    
    

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

        c = (int((x1 + x2)/2),int((y1 + y2)/2))
        r = int(np.sqrt((x2-x1)**2)/2)
        draw_circles(img, c, r, x1, y1, x2, y2)
        

# Create a white image and a window
img = np.zeros((720, 720, 3), np.uint8) + 255
cv2.namedWindow('Rectangle Drawer')

# Bind the mouse callback function to window
cv2.setMouseCallback('Rectangle Drawer', draw_square)

while True:
    cv2.imshow('Rectangle Drawer', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
