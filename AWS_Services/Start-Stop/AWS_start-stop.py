"""
During the execution of this code we have to update the instance_id and file-name along with actions which we want to perform.

**** This can be done with existing instances which are currently in 'running or stopped' state.****
"""

import sys
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')

if action == 'ON':
	# Do a dryrun first to verify permissions
	try:
		ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise

	# Dry ryn succeeded, run start_instance without dryrun
	try:
		response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
		print(f"The existing instance {instance_id} is now started.\n")
		print(response)
	except ClientError as e:
		print(e)
else:
	# Do a dryrun first to verify permissions
	try:
		ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise

	# Dry run succeeded, run stop_instance without dryrun
	try:
		response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
		print(f"The existing instance {instance_id} is now stopped.\n")
		print(response)
	except ClientError as e:
		print(e)