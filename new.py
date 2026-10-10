
import boto3

# Create session using ~/.aws/credentials
session = boto3.Session(profile_name="default")

# Create EC2 resource and client
ec2 = session.resource("ec2")
client = session.client("ec2")

# Display existing VPCs
print("\nExisting VPCs:")
for vpc in ec2.vpcs.all():
    print(f"VPC ID: {vpc.id}, CIDR: {vpc.cidr_block}, State: {vpc.state}")

# Ask user whether to create a new VPC
choice = input("\nDo you want to create a new VPC? (yes/no): ").strip().lower()

if choice == "yes":
    cidr = input("Enter the CIDR range (example: 10.0.0.0/16): ").strip()

    try:
        # Create the VPC
        response = client.create_vpc(CidrBlock=cidr)

        vpc_id = response["Vpc"]["VpcId"]

        # Wait until the VPC becomes available
        new_vpc = ec2.Vpc(vpc_id)
        new_vpc.wait_until_available()

        print("\nVPC created successfully!")
        print("VPC ID:", vpc_id)
        print("CIDR Range:", cidr)
        print("State:", new_vpc.state)

    except Exception as e:
        print("Error creating VPC:", e)

elif choice == "no":
    print("Exiting program. No VPC created.")

else:
    print("Invalid choice. Please run the program again and enter yes or no.")
