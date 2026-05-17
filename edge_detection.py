import cv2
import numpy as np

# Start capturing video from the default webcam (device index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define a 5x5 kernel of ones, used for dilation and erosion
kernel = np.ones((5, 5), np.uint8)

# Read and process frames in a continuous loop
while True:
    # Read one frame from the webcam
    # 'ret' is True if the frame was captured successfully
    ret, frame = cap.read()

    # If the frame was not captured, skip to the next iteration
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the colour frame to grayscale
    # Grayscale is required for Canny edge detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    # 100 = lower threshold, 200 = upper threshold
    edges = cv2.Canny(gray_frame, 100, 200)

    # Apply dilation — expands the white edge pixels outward
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # Apply erosion — shrinks the white edge pixels inward
    eroded = cv2.erode(edges, kernel, iterations=1)

    # Display each result in its own window
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Edges", edges)
    cv2.imshow("Dilated Edges", dilated)
    cv2.imshow("Eroded Edges", eroded)

    # Wait 1 millisecond for a key press
    # If the user presses 'q', exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam so other applications can use it
cap.release()

# Close all OpenCV display windows
cv2.destroyAllWindows()
