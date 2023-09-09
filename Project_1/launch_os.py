import boto3

my_ec2 = boto3.resource('ec2')

def Launch_OS():
	response = my_ec2.create_instances(
		ImageId="ami-0da59f1af71ea4ad2",
		InstanceType="t2.micro",
		MaxCount=1,
		MinCount=1
)