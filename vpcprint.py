
import boto3

# Read AWS credentials from ~/.aws/credentials
session = boto3.Session(profile_name="default")

# Create EC2 resource using the session
ec2 = session.resource("ec2")

# Get all VPCs
vpcs = ec2.vpcs.all()

# Print all VPCs
print("List of VPCs:")

for vpc in vpcs:
    print("VPC ID:", vpc.id)
    print("CIDR Block:", vpc.cidr_block)
    print("State:", vpc.state)
    print("-" * 40)
