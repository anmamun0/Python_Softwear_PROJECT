import cv2
import time

# Load the pre-trained face and smile cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Open the camera
camera = cv2.VideoCapture(0)

# Initialize smile status and start time
smile_status = False
start_time = None

while True:
    # Read the current frame from the camera
    ret, frame = camera.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        # Extract the region of interest (ROI) from the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect smiles within the face region
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20, minSize=(30, 30))

        # Iterate over detected smiles
        for (sx, sy, sw, sh) in smiles:
            # Draw rectangles around the detected faces and smiles
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
            smile_status = True

            # Start the timer if it hasn't been started yet
            if start_time is None:
                start_time = time.time()

    # Display the frame
    cv2.imshow('Smile Detection', frame)

    # Check if a smile is detected continuously for 2 seconds
    if smile_status and time.time() - start_time > 2:
        # Save the selfie image
        cv2.imwrite('selfie.jpg', frame)
        print("Selfie captured!")
        break

    # Reset smile status and start time if no smile is detected
    if not smile_status:
        start_time = None

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
