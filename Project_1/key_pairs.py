# Working with amazon EC2 service Key-Pairs
import boto3

key_pair_name = "Advanced-Keys"
my_ec2 = boto3.client('ec2')

def keys_describe():
	response = my_ec2.describe_key_pairs()
	print(response)

def keys_create():
	response = my_ec2.create_key_pair(KeyName=key_pair_name)
	print(f"\nThe new {key_pair_name} has created. :\n\n")
	keys_describe()

def keys_delete():
	response = my_ec2.delete_key_pair(KeyName=key_pair_name)
	print(f"\nThe new {key_pair_name} has removed. :\n\n")
	keys_describe()

# keys_create()
# keys_delete()