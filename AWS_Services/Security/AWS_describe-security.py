import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
SECURITY_GROUP_ID = 'sg-021b1e1e77860ecfe'

try:
	response = ec2.describe_security_groups(GroupIds=[SECURITY_GROUP_ID])
	print("\n", response)
except ClientError as e:
	print(e)