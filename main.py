from CircleCounters import *

# initialize the camera capture object
cap = cv2.VideoCapture(2)

# set the camera resolution to 1280x720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# loop through each frame of the camera feed
while True:
    # read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break
    # count the number of red circles in the frame

    blue_circle_count = count_blue_circles(frame)
    greenInBlue_circle_count = count_greeninblue_circles(frame)
    greenInBlack_circle_count = count_greeninblack_circles(frame)
    yellow_circle_count = count_yellow_circles(frame)

    # display the result on the screen
    cv2.putText(frame, f"greenInBlue: {greenInBlue_circle_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"greenInBlack: {greenInBlack_circle_count}", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Yellow circles: {yellow_circle_count}", (500, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Camera Feed", frame)
    # press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break

# release the camera capture object and close the display window
cap.release()
cv2.destroyAllWindows()