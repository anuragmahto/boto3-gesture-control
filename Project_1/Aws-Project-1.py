# Python Used Libraries

import boto3 
import sys
import time 
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	exit()

detect = HandDetector()

delay = 0
start_time = time.time() # for taking current time

while True:
	ret, photo = cap.read()
	photo = cv2.flip(photo, 1)

	if not ret:
		break

	cv2.imshow("Display-Screen", photo)
	if cv2.waitKey(1) & 0xff == ord('b'):
		break

	hand_photo = detect.findHands(photo, draw=False)

	if time.time() - start_time > delay:
		if hand_photo:
			# lmlist is the list of lm object with a common model
			lmlist = hand_photo[0]
			fingerstatus = detect.fingersUp(lmlist)
			delay = 5
			start_time = time.time()

			if fingerstatus == [1,0,0,0,0]:
				print("\nThumbs Up")
			elif fingerstatus == [1,1,0,0,0]:
				print("\nThumb & Index Up")
			elif fingerstatus == [1,1,1,0,0]:
				print("\nThumb & Index & Middle Up")
			elif fingerstatus == [0,1,0,0,0]:
				print("\nIndex Up")
			elif fingerstatus == [0,1,1,0,0]:
				print("\nIndex & Middle Up")
			elif fingerstatus == [0,1,1,1,0]:
				print("\nIndex & Middle & Ring Up")
			elif fingerstatus == [0,1,1,1,1]:
				print("\nIndex & Middle & Ring & Little Up")
			elif fingerstatus == [1,1,1,1,1]:
				print("\nAll Up")
			else:
				delay = 0
cap.release()
cv2.destroyAllWindows()