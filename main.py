import os
import cv2
import numpy as np

from mediapipe.python.solutions import selfie_segmentation
from utils import stackImages

# Initialize MediaPipe Selfie Segmentation (model_selection=0 → general environment)
selfie_segmentor = selfie_segmentation.SelfieSegmentation(model_selection=0)

# Open webcam (device 0) and set FPS to 60 for smoother streaming
webcam = cv2.VideoCapture(0)
webcam.set(propId=cv2.CAP_PROP_FPS, value=60)

# Load all background images from the "backgrounds" directory
files_list = os.listdir(path="backgrounds")
backgrounds = []
for file in files_list:
    background = cv2.imread(filename=f"backgrounds/{file}")
    backgrounds.append(background)

# Current background index (used to cycle through loaded backgrounds)
index = 0


def empty(e):
    """Placeholder function for the trackbar callback (not used)."""
    pass


# Create a display window and add a trackbar for segmentation threshold adjustment
cv2.namedWindow(winname="stacked images")
cv2.createTrackbar("Threshold", "stacked images", 75, 100, empty)


while True:
    # Capture frame from webcam
    is_successful, frame = webcam.read()
    if not is_successful:
        break

    # Convert frame from BGR → RGB for MediaPipe
    rgb_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)

    # Run MediaPipe segmentation
    results = selfie_segmentor.process(image=rgb_frame)
    mask = results.segmentation_mask

    # Smooth the mask for softer edges
    mask = cv2.GaussianBlur(src=mask, ksize=(21, 21), sigmaX=0)

    # Get threshold value from trackbar (0.0 → 1.0)
    threshold = (
        cv2.getTrackbarPos(trackbarname="Threshold", winname="stacked images") / 100
    )

    # Create boolean condition mask (True = foreground, False = background)
    condition = np.stack(arrays=(mask,) * 3, axis=2) > threshold

    # Replace background using the selected image
    output_frame = np.where(condition, frame, backgrounds[index])

    # Stack original and output frames side by side for comparison
    stacked_images = stackImages(rows=[[frame, output_frame]], scale=1)
    cv2.imshow(winname="stacked images", mat=stacked_images)

    # Keyboard controls
    key = cv2.waitKey(delay=1)

    if key == 27:  # ESC → Exit
        break
    elif key == ord("n") or key == ord("N"):  # Next background
        if index < len(backgrounds) - 1:
            index += 1
    elif key == ord("p") or key == ord("P"):  # Previous background
        if index > 0:
            index -= 1

# Release resources
webcam.release()
cv2.destroyAllWindows()
