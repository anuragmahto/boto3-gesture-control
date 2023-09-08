import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
try:
	Instance_id = 'i-014b72e77364b4bb8'
	allocate = ec2.allocate_address(Domain='vpc')
	response = ec2.associate_address(AllocationId=allocate['AllocationId'], InstanceId=Instance_id)
	print("\n", response, "\n")

except ClientError as e:
	print(e)