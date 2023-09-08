# This is used to create our own customized policy based on our requirements.

import json 
import boto3

iam = boto3.client('iam')

def policy_create():
	my_managed_policy = {"Version": "2012-10-17", "Statement":[{"Effect":"Allow", "Action":"logs:CreateLogGroup",
		"Resource":"arn:aws:iam::622782999923:user/Mohit"}, 
		{"Effect":"Allow", "Action":["dynamodb:DeleteItem", "dynamodb:GetItem", "dynamodb:PutItem", "dynamodb:Scan", "dynamodb:UpdateItem"], 
		"Resource": "arn:aws:iam::622782999923:user/Mohit"}]
	}

	response = iam.create_policy( PolicyName='myDynamoDBPolicy', PolicyDocument=json.dumps(my_managed_policy) )
	print("\n", response)

def policy_list():
	response = iam.get_policy(PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess")
	print("\n", response)

# def role_attach():
# 	iam.attach_role_policy(PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess", RoleName="AdministratorAccess")
# 	print("\nSuccessfully Attatched\n")

# def role_detach():
# 	iam.detach_role_policy(PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',RoleName='AdministratorAccess')
# 	print("\nSuccessfully Dettatched\n")

policy_create()
policy_list()

# role_attach()
# role_detach()
