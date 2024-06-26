"""
There are three things we can do with the instances: 
--> Launch OS 
--> Start-Reboot existing instance 
--> Stop instance
"""


# Python Used Libraries
import boto3
import sys
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

my_ec2 = boto3.client('ec2')

#	During execution of the code we have to update instance_id & file-name along with actions which we want to perform. #
# 	Below functions are for existing Instances only.

def Start_Stop():
	if action == "ON":
		# Do a dry run 
		try:
			my_ec2.create_instances(InstanceIds=[instance_id], DryRun=True)
		except ClientError as e:
			if 'DryRunOperation' not in str(e):
				raise

		# Dry Run success, then run without dryrun
		try:
			response = my_ec2.create_instances(InstanceIds=[instance_id], DryRun=False)
			print(f"\nThe exsisting instance {instance_id} is now active.\n")
			print(response)
		except ClientError as e:
			print(e)
	else:
		# Do a dry run
		try:
			my_ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
		except ClientError as e:
			if 'DryRunOperation' not in str(e):
				raise

		# Dry Run success, then run without dryrun
		try:
			response = my_ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
			print(f"\nThe exsisting instance {instance_id} is now deactive.\n")
			print(response)
		except ClientError as e:
			print(e)

def Reboot():
	# Do a dry run
	try:
		my_ec2.reboot_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise

	# Dry Run success, then run without dryrun
	try:
		response = reboot_instances(InstanceIds=[instance_id], DryRun=False)
		print(f"\nThe exsisting instance {instance_id} is now rebooted.\n")
		print(response)
	except ClientError as e:
		print(e)

# Launch_OS()

# Start_Stop()

# Reboot()