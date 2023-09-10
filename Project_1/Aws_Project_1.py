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
	
	# text = "Press 'b' to exit"
	# cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

	# cv2.imshow("Display-Screen", photo)
	# if cv2.waitKey(1) & 0xff == ord('b'):
	# 	break

	hand_photo = detect.findHands(photo, draw=False)
	if time.time() - start_time > delay:
		if hand_photo:
			# lmlist is the list of lm object with a common model
			lmlist = hand_photo[0]
			fingerstatus = detect.fingersUp(lmlist)
			
			delay = 5
			start_time = time.time()

			if fingerstatus == [1,0,0,0,0]:
				# print("\nLaunching an OS on Cloud.")
				Launch_OS()
				text = "Launching an Os on Cloud."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [1,1,0,0,0]:
				# print("\nIam User Created.")
				user_create()
				text = "Iam User Created."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [1,1,1,0,0]:
				# print("\nIam User Updated.")
				user_update()
				text = "Iam User Updated."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [0,1,0,0,0]:
				# print("\nS3 Bucket Created.")
				bucket_create()
				text = "S3 Bucket Created."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [0,1,1,0,0]:
				# print("\nS3 Bucket Removed.")
				bucket_delete()
				text = "S3 Bucket Removed."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [0,1,1,1,0]:
				# print("\nEC2 Keys Created.")
				keys_create()
				text = "EC2 Keys Created."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [0,1,1,1,1]:
				# print("\nUpdated User Removed.")
				upd_user_delete()
				text = "Iam Updated User Removed."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)

			elif fingerstatus == [1,1,1,1,1]:
				# print("\nKeys and Created user Removed.")
				keys_delete()
				user_delete()
				text = "Keys and Created User Removed."
				cv2.putText(photo,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,255,212),2)
				
			else:
				delay = 0
	cv2.imshow("Display-Screen", photo)
	if cv2.waitKey(1) & 0xff == ord('b'):
		break
cap.release()
cv2.destroyAllWindows()