import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    instance_id = 'i-014b72e77364b4bb8'
    allocate = ec2.allocate_address(Domain='vpc')
    response = ec2.release_address(AllocationId=allocate['AllocationId'])
    print('\nAddress released..\n')

except ClientError as e:
    if e.response['Error']['Code'] == 'AddressLimitExceeded':
        # If you've reached the maximum limit, try to release an unused Elastic IP
        print('Address limit reached. Trying to release an unused Elastic IP...')
        addresses = ec2.describe_addresses()
        for address in addresses['Addresses']:
            if 'InstanceId' not in address:
                # This Elastic IP is not associated with any instance, so it's unused
                ec2.release_address(AllocationId=address['AllocationId'])
                print('Released an unused Elastic IP.')
                # Now, retry the allocation
                allocate = ec2.allocate_address(Domain='vpc')
                response = ec2.release_address(AllocationId=allocate['AllocationId'])
                print('\nAddress released Successfully..!!\n')
                break
    else:
        # If the error is not "AddressLimitExceeded", print the error message
        print(e)
