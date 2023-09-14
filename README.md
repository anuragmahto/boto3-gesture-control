# PyAWS Cloud Ops

PyAWS Cloud Ops is a unique project that allows you to control cloud operations using hand gestures. This Python-based application leverages computer vision and Amazon Web Services (AWS) to provide a gesture-driven interface for cloud management.

## Overview

The application supports the following gestures:
* Launch an OS on a cloud server
* Create and manage IAM users
* Create and delete S3 buckets
* Generate and manage EC2 key pairs

With just a few simple hand gestures, you can interact with your AWS resources, making cloud administration more intuitive and efficient.

## Features
* Gesture-based control of AWS operations
* Real-time hand tracking and gesture recognition
* Quick access to common cloud tasks
* User-friendly and interactive interface
* Integration with AWS services

## Usage
1 Ensure you have the required Python libraries and AWS credentials set up.
[Follow this link to setup your aws account credentials.] (https://docs.aws.amazon.com/cli/latest/reference/configure/)

2 Run the main.py script to start the application.

3 Use hand gestures to control AWS operations based on the gesture key mapping.

***

## Installation
1 Clone this repository to your local machine.

2 Install the necessary Python libraries using
 ```python 
pip install -r requirements.txt
```
3 Configure your AWS credentials in the appropriate AWS configuration file.
***

## Dependencies
* Python 3.8.10
* OpenCV
* boto3
* cvzone
