import boto3

iam = boto3.client('iam')

def user_create():
	name = 'Harshit'
	response = iam.create_user(UserName=name)
	print("\n",response,"\n")
	print(f"The user {name} has been successfully created.#")

def user_list():
	paginator = iam.get_paginator('list_users')
	for response in paginator.paginate():
		print(response)

def user_update():
	name = 'Anurag'
	iam.update_user(UserName='Ownis', NewUserName=name)
	print(f"This IAM user {name} is now updated with {NewUserName}.")

def user_delete():
	name = 'Yash'
	iam.delete_user(UserName=name)
	print(f"This IAM user {name} has been successfully delted..!!")

#user_create()
#user_list()
#user_update()
#user_delete()
