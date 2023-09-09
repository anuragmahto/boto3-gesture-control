# Importing functions from different files in this main file

from launch_os import Launch_OS
from iam_user import user_create,user_delete,user_update,upd_user_delete
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
				print("\nLaunching an OS on Cloud.")
				Launch_OS()

			elif fingerstatus == [1,1,0,0,0]:
				print("\nIam User Created.")
				user_create()

			elif fingerstatus == [1,1,1,0,0]:
				print("\nIam User Updated.")
				user_update()

			elif fingerstatus == [0,1,0,0,0]:
				print("\nS3 Bucket Created.")
				bucket_create()

			elif fingerstatus == [0,1,1,0,0]:
				print("\nS3 Bucket Removed.")
				bucket_delete()

			elif fingerstatus == [0,1,1,1,0]:
				print("\nEC2 Keys Created.")
				keys_create()

			elif fingerstatus == [0,1,1,1,1]:
				print("\nEC2 Keys Removed.")
				keys_delete()

			elif fingerstatus == [1,1,1,1,1]:
				print("\nUpdated and Created user Removed.")
				upd_user_delete()
				user_delete()
				
			else:
				delay = 0
cap.release()
cv2.destroyAllWindows()