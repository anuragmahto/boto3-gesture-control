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

def fingersUp():
	return True

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	exit()

detect = HandDetector()

delay = 0
start_time = time.time() # for taking current time

text=""
text_Smooth = 3.0
text_showing = False
text_off = 0.0

while True:
	ret, photo = cap.read()
	photo = cv2.flip(photo, 1)

	if not ret:
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
				Launch_OS()
				text = "Launching an Os on Cloud."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [1,1,0,0,0]:
				user_create()
				text = "Iam User Created."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [1,1,1,0,0]:
				user_update()
				text = "Iam User Updated."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [0,1,0,0,0]:
				bucket_create()
				text = "S3 Bucket Created."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [0,1,1,0,0]:
				bucket_delete()
				text = "S3 Bucket Removed."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [0,1,1,1,0]:
				keys_create()
				text = "EC2 Keys Created."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [0,1,1,1,1]:
				upd_user_delete()
				text = "Iam Updated User Removed."
				text_off = time.time() + text_Smooth

			elif fingerstatus == [1,1,1,1,1]:
				keys_delete()
				user_delete()
				text = "Keys and Created User Removed."
				text_off = time.time() + text_Smooth
				
			else:
				delay = 0
				text_showing = False

		if fingersUp():
			text_showing = True
			
	if text_showing and time.time() < text_off:
		cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,114,86),2)
	else:
		text_showing = False

	scale_percent = 150
	width = int(photo.shape[1] * scale_percent / 100)
	height = int(photo.shape[0] * scale_percent / 100)
	dim = (width, height)
	photo_resized = cv2.resize(photo, dim, interpolation = cv2.INTER_AREA)

	cv2.imshow("Display-Screen", photo_resized)
	if cv2.waitKey(1) & 0xff == ord('b'):
		break

cap.release()
cv2.destroyAllWindows()