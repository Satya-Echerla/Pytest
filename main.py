import boto3
import pytest

session = boto3.Session(
    aws_access_key_id='AKIAU5JMI6OHEMKMEM3R',
    aws_secret_access_key='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',
)

ec2 = session.client('ec2', region_name='us-east-2')


@pytest.fixture
def get_ec2_instance():
    # Specify the instance ID
    instance_id = 'i-087bf1dc3867f4688'
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
    assert instance['InstanceId'] == 'i-087bf1dc3867f4688'
