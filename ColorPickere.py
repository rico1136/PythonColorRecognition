import cv2
import numpy as np

color_explore = np.zeros((150, 150, 3), np.uint8)
color_selected = np.zeros((150, 150, 3), np.uint8)


# save selected color RGB in file
def write_to_file(R, G, B):
    f = open("saved_color.txt", "a")
    RGB_color = str(R) + "," + str(G) + "," + str(B) + str("\n")
    f.write(RGB_color)
    f.close()


# Mouse Callback function
def show_color(event, x, y, flags, param):
    B = img[y, x][0]
    G = img[y, x][1]
    R = img[y, x][2]
    color_explore[:] = (B, G, R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected[:] = (B, G, R)

    if event == cv2.EVENT_RBUTTONDOWN:
        B = color_selected[10, 10][0]
        G = color_selected[10, 10][1]
        R = color_selected[10, 10][2]
        print(R, G, B)
        write_to_file(R, G, B)
        print(hex(R), hex(G), hex(B))


# live update color with cursor
cv2.namedWindow('color_explore')
cv2.resizeWindow("color_explore", 50, 50);

# Show selected color when left mouse button pressed
cv2.namedWindow('color_selected')
cv2.resizeWindow("color_selected", 50, 50);

# image window for sample image
cv2.namedWindow('image')

# initialize the camera capture object
cap = cv2.VideoCapture(3)

# set the camera resolution to 1280x720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# mouse call back function declaration
cv2.setMouseCallback('image', show_color)

# loop through each frame of the camera feed
while True:
    # read a frame from the camera
    ret, img = cap.read()

    cv2.imshow('image', img)
    cv2.imshow('color_explore', color_explore)
    cv2.imshow('color_selected', color_selected)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    if not ret:
        break


# release the camera capture object and close the display window
cap.release()
cv2.destroyAllWindows()
