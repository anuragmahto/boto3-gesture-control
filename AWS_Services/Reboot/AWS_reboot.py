import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
Instance_Id = sys.argv[1]
try:
	ec2.reboot_instances(InstanceIds=[Instance_Id], DryRun=True)
except ClientError as e:
	if 'DryRunOperation' not in str(e):
		print("You don't have permission to reboot instance.\n")
		raise
try:
	response = ec2.reboot_instances(InstanceIds=[Instance_Id], DryRun=False)
	print('Successful\n\n',response)
except ClientError as e:
	print('Error\n',e)