# Working with amazon S3 service Bucket
import boto3

# We have to set these values at the beginning everytime 
AWS_REGION = "ap-south-1"
my_bucket = boto3.client('s3', region_name=AWS_REGION)

bucket_name = "bucket-my-project"
Bucket = bucket_name

location = {'LocationConstraint': AWS_REGION}

def bucket_list():
	response = my_bucket.list_buckets()
	print("\nAvailable Buckets : ")
	for bucket in response['Buckets']:
		print(f'-- {bucket["Name"]}')

def bucket_create():
	response = my_bucket.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
	print(f"\nThe bucket {bucket_name} has created.")
	bucket_list()

def bucket_delete():
	my_bucket.delete_bucket(Bucket=bucket_name)
	print(f"\nThe bucket {bucket_name} has removed.")
	bucket_list()

# bucket_create()
# bucket_delete()