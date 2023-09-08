import boto3

ec2 = boto3.client('ec2')

def Region():
	response = ec2.describe_regions()
	print('\nRegions :', response['Regions'])

def Zone():
	response2 = ec2.describe_availability_zones()
	print('\nAvailability_Zones :', response2['AvailabilityZones'])

Region()
Zone()