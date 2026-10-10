
import boto3

session = boto3.Session(profile_name="default")
ec2 = session.resource("ec2")

# Print existing VPCs
for vpc in ec2.vpcs.all():
    print(vpc.id, vpc.cidr_block)

# Ask user
choice = input("Do you want to create a new VPC? (yes/no): ")

if choice.lower() == "yes":
    cidr = input("Enter CIDR range: ")
    vpc = ec2.create_vpc(CidrBlock=cidr)
    vpc.wait_until_available()
    print("VPC created:", vpc.id)

else:
    print("Exiting...")
