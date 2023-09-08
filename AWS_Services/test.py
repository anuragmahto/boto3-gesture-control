# Creating S3 Bucket using Boto3 client

import boto3
import time

import sys
sys.path.insert(0, '/home/anurag/AWS_Services/IAM')
print(sys.path)
from IAM_keys import *

AWS_REGION = "ap-south-1"
client = boto3.client("s3", region_name=AWS_REGION)
bucket_name = "my-first-bucket-three"
Bucket = bucket_name
location = {'LocationConstraint': AWS_REGION}

def BucketCreation():
	response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

# Listing S3 Buckets using Boto3 client

def ListingBuckets():
	response = client.list_buckets()
	print("\nLisitng all Amazon s3 buckets : ")
	for bucket in response['Buckets']:
		print(f'-- {bucket["Name"]}')

# Delete Amazon S3 Bucket using Boto3

def DeletingBuckets():
	client.delete_bucket(Bucket=bucket_name)
	print("Amazon s3 bucket has been deleted!")

import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("Error: Could not find WebCam..!!")
	exit()

from cvzone.HandTrackingModule import HandDetector
detector = HandDetector()
DELAY_SECONDS = 0
start_time = time.time() # taking current time

while True:
        ret, photo = cap.read()
        photo = cv2.flip(photo, 1)

        if not ret:
        	print("Error: Could not read frame.")
        	break

        cv2.imshow("my photo", photo)
        if cv2.waitKey(1) & 0xff == ord('b'):
        	break

        handphoto = detector.findHands(photo, draw=False)
        if time.time() - start_time > DELAY_SECONDS:
            if handphoto:
                _list = handphoto[0]
                fingerstatus = detector.fingersUp(_list)
                DELAY_SECONDS = 5
                start_time = time.time()

                if fingerstatus == [0, 1, 0, 0, 0]:
                    print("\nIndex Finger Up")
                    BucketCreation()

                elif fingerstatus==[0, 1, 1, 0, 0]:
                    print("\nTwo Fingers Up")
                    ListingBuckets()

                elif fingerstatus == [1, 1, 1, 1, 1]:
                    print("\nAll Fingers Up")
                    DeletingBuckets()
                    #break
                else:
                    DELAY_SECONDS = 0

cap.release()
cv2.destroyAllWindows()