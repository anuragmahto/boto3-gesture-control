# Importing functions from different files in this main file

from launch_os import Launch_OS
from iam_user import user_create,user_delete,user_update
from bucket import bucket_create, bucket_delete
from key_pairs import keys_create, keys_delete

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
				Launch_OS()

			elif fingerstatus == [1,1,0,0,0]:
				print("\nThumb & Index Up")
				user_create()

			elif fingerstatus == [1,1,1,0,0]:
				print("\nThumb & Index & Middle Up")
				user_update()

			elif fingerstatus == [0,1,0,0,0]:
				print("\nIndex Up")
				bucket_create()

			elif fingerstatus == [0,1,1,0,0]:
				print("\nIndex & Middle Up")
				bucket_delete()

			elif fingerstatus == [0,1,1,1,0]:
				print("\nIndex & Middle & Ring Up")
				keys_create()

			elif fingerstatus == [0,1,1,1,1]:
				print("\nIndex & Middle & Ring & Little Up")

			elif fingerstatus == [1,1,1,1,1]:
				print("\nAll Up")
				keys_delete()
				user_delete()

			else:
				delay = 0
cap.release()
cv2.destroyAllWindows()