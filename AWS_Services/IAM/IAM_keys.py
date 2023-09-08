import boto3

iam = boto3.client('iam')

def create():
	response = iam.create_access_key(UserName="Mohit")
	print("\n", response['AccessKey'])

def klist():
	paginator = iam.get_paginator('list_access_keys')
	for response in paginator.paginate(UserName='Mohit'):
		print("\n", response)

def lastused():
	response = iam.get_access_key_last_used(AccessKeyId="AKIAZCAGCNVZTV2PSI53")
	#response = iam.get_access_key_last_used(AccessKeyId="AKIAZCAGCNVZ2GRIUB5I")
	print("\n", response['AccessKeyLastUsed'])

def updatestatus():
	iam.update_access_key(AccessKeyId="AKIAZCAGCNVZTV2PSI53", Status="Active", UserName="Mohit")
	print("\nSuccessfully Updates the access keys.\n")

def delete():
	key_id = "AKIAZCAGCNVZ2GRIUB5I"
	iam.delete_access_key(AccessKeyId=key_id)
	print(f"\nSuccessfully Deleted Key : {key_id}\n")


#create()
#klist()
#lastused()
#updatestatus()
#delete()