"""
1. How to read ram
"""

"""
import os
var = "Data"
print(var)

os.system("chrome")

name_data = ["Anurag","Rahul","Vishal","Krihsna"]
print(name_data)

var_x = 15
"""



import cv2
import os
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)  # Connect to your webcam
status, photo = cap.read()  # Capture an image from the webcam

# Check if the image is captured successfully
if status:
    detector = HandDetector(detectionCon=0.8, maxHands=2)   # Adjust parameters as needed
    hands, photo = detector.findHands(photo)

    if hands and len(hands) > 0:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        if fingers == [1,1,1,1,1]:
            print("All Up")
        elif fingers == [0,1,0,0,0]:
        	print("index finger up")
        elif fingers == [0,1,1,0,0]:
        	print("index and middle finger up")
        else:
        	print("Nothing Happens")


    cv2.imshow("My Image", photo)
    cv2.waitKey(5000)  # Display the image for 5 seconds

    cv2.imwrite("Anurag.jpg", photo)
    print("Image captured and saved as Anurag.jpg")
else:
    print("Image capture failed")

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all open windows
