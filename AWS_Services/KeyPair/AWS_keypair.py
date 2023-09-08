import boto3

key_pair_name = "New-Keys"
ec2 = boto3.client('ec2')

def create(): 
	response1 = ec2.create_key_pair(KeyName=key_pair_name)
	print("\nSuccessfully create new KeyPair : \n\n",response1)

def describe():
	response2 = ec2.describe_key_pairs()
	print(response2)

def delete():
	response3 = ec2.delete_key_pair(KeyName=key_pair_name)
	print("\nSuccessfully deleted new KeyPair : \n\n", response3)

# Remove the comment which action you want to perform  
#create()
#describe()
#delete()