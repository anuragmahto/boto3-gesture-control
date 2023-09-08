# IAM users 
import boto3

my_iam = boto3.client('iam')

def user_list():
	paginator = my_iam.get_paginator('list_users')
	for response in paginator.paginate():
		print(response,"\n")

def user_create():
	name = "Harshit"
	response = my_iam.create_user(UserName=name)
	print(f"\nThe user {name} has created.\n")
	print(response,"\n")
	user_list()

def user_update():
	name = "Abhinaw"
	my_iam.update_user(UserName='Harshit', NewUserName=name)
	print(f"The user {name} has updated.\n")
	user_list()

def user_delete():
	name = "Harshit"
	my_iam.delete_user(UserName=name)
	print(f"\nThe user {name} has removed.\n")
	user_list()

# user_create()
# user_list()
# user_update()
# user_delete()