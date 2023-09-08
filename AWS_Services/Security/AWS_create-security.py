import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
Security_Group_Name = 'New-Security' # Add a non-existing name in the security groups
Descrip = 'New-Level' # Anything about the group which you want to describe

try:
	response = ec2.create_security_group(GroupName=Security_Group_Name, Description=Descrip, VpcId=vpc_id)
	security_group_id=response['GroupId']
	print(f"\nSecurity Group has been created {security_group_id} in vpc {vpc_id}")

	data = ec2.authorize_security_group_ingress(
		GroupId=security_group_id,
		IpPermissions=[
		{'IpProtocol':'tcp', 'FromPort':80, 'ToPort':80, 'IpRanges':[{'CidrIp':'0.0.0.0/0'}]},
		{'IpProtocol':'tcp', 'FromPort':22, 'ToPort':22, 'IpRanges':[{'CidrIp':'0.0.0.0/0'}]}
		]
	)
	print(f"\nIngress Successfully set {data}")
except ClientError as e:
	print(e)