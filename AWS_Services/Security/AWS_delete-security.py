import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
security_group_id='sg-0f8e7a2d47d6bf6f4' # replace the group id which you want to delete.

try:
	response = ec2.delete_security_group(GroupId=security_group_id)
	print("\nSecurity Group deleted...!!!")
except ClientError as e:
	print(e)