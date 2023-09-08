"""
Replace the INSTANCE_ID with the provided instance_id by aws.
"""

# This is used to enable detailed monitoring.

import boto3
import sys

ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
	response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
	response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)