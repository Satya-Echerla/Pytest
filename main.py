import boto3
import pytest

session = boto3.Session(
    aws_access_key_id='abc',
    aws_secret_access_key='12345',
)

ec2 = session.client('ec2', region_name='us-east-2')


@pytest.fixture
def get_ec2_instance():
    # Specify the instance ID
    instance_id = '1'
    # Get the instance
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]
    # Return the instance
    yield instance

def test_get_ec2_instance(get_ec2_instance):
    # Use the instance returned by the fixture
    instance = get_ec2_instance
    # Check that the instance exists
    assert instance is not None
    # Check that the instance has the correct ID
    assert instance['InstanceId'] == '1'
