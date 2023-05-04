import cv2
import numpy as np

# define the initial lower and upper limits of the color range
init_lower = np.array([100, 100, 100])
init_upper = np.array([120, 255, 255])


# create a function to update the color range based on the trackbar values
def update_range(x):
    # get the current trackbar values
    h_min = cv2.getTrackbarPos("H_min", "Color Range")
    s_min = cv2.getTrackbarPos("S_min", "Color Range")
    v_min = cv2.getTrackbarPos("V_min", "Color Range")
    h_max = cv2.getTrackbarPos("H_max", "Color Range")
    s_max = cv2.getTrackbarPos("S_max", "Color Range")
    v_max = cv2.getTrackbarPos("V_max", "Color Range")

    # update the lower and upper limits of the color range
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # display the current color range on the image
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Color Range", result)


# create a VideoCapture object to capture frames from the camera
cap = cv2.VideoCapture(3)

# create a window to display the color range
cv2.namedWindow("Color Range")

# create trackbars to adjust the color range limits
cv2.createTrackbar("H_min", "Color Range", init_lower[0], 255, update_range)
cv2.createTrackbar("S_min", "Color Range", init_lower[1], 255, update_range)
cv2.createTrackbar("V_min", "Color Range", init_lower[2], 255, update_range)
cv2.createTrackbar("H_max", "Color Range", init_upper[0], 255, update_range)
cv2.createTrackbar("S_max", "Color Range", init_upper[1], 255, update_range)
cv2.createTrackbar("V_max", "Color Range", init_upper[2], 255, update_range)


while True:
    # read a frame from the camera
    ret, frame = cap.read()

    # convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # wait for a key press and check if the 'q' key was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
