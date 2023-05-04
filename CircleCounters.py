import cv2
import numpy as np

# Set minimum and max HSV values to display
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 31])

# define the blue color range in HSV format
lower_blue = np.array([80, 150, 75])
upper_blue = np.array([140, 255, 255])

# define the lower and upper green color ranges in HSV color space
lower_green = np.array([35, 50, 50])
upper_green = np.array([75, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

blur_size = 11
blur_sigma = 0


def count_greeninblue_circles(img):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Apply image preprocessing by blurring the image
    blurred = cv2.GaussianBlur(hsv, (blur_size, blur_size), blur_sigma)

    # Apply the green and white color masks
    mask_blue = cv2.inRange(blurred, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Apply image processing to remove noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask_blue = cv2.dilate(mask_blue, kernel, iterations=2)

    # Apply image processing to remove noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask_green = cv2.dilate(mask_green, kernel, iterations=2)

    mask_combined = cv2.bitwise_or(mask_green, mask_blue)



    # Find contours of green circles
    contours, hierarchy = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours and count the green circles
    circle_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # adjust this threshold as needed
            # Find the center and radius of the contour
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Check if the green circle is surrounded by white in the combined mask
            mask_roi = mask_combined[int(y-radius):int(y+radius), int(x-radius):int(x+radius)]
            if np.all(mask_roi != 0):
                # Draw the outline of the green circle
                cv2.circle(img, center, radius, (0, 255, 0), 2)
                # Put text on the green circle
                cv2.putText(img, "Blue in green", (center[0] - 50, center[1] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                            2)
                circle_count += 1

    cv2.imshow("Blue mask", mask_blue)
    cv2.imshow("Green mask", mask_green)
    cv2.imshow("Combined mask", mask_combined)

    # Return the number of green circles
    return circle_count


def count_greeninblack_circles(img):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Apply image preprocessing by blurring the image
    blurred = cv2.GaussianBlur(hsv, (blur_size, blur_size), blur_sigma)

    # Apply the green and white color masks
    mask_black = cv2.inRange(blurred, lower_black, upper_black)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Apply image processing to remove noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask_black = cv2.dilate(mask_black, kernel, iterations=2)

    # Apply image processing to remove noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask_green = cv2.dilate(mask_green, kernel, iterations=2)

    mask_combined = cv2.bitwise_or(mask_green, mask_black)



    # Find contours of green circles
    contours, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours and count the green circles
    circle_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # adjust this threshold as needed
            # Find the center and radius of the contour
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Check if the green circle is surrounded by white in the combined mask
            mask_roi = mask_combined[int(y-radius):int(y+radius), int(x-radius):int(x+radius)]
            if np.all(mask_roi != 0):
                # Draw the outline of the green circle
                cv2.circle(img, center, radius, (0, 255, 0), 2)
                # Put text on the green circle
                cv2.putText(img, "green in black", (center[0] - 50, center[1] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                            2)
                circle_count += 1

    # Return the number of green circles
    return circle_count



def count_blue_circles(img):

    return 0


def count_yellow_circles(img):


    return 0
