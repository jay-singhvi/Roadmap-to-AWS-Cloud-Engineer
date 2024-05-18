# Roadmap to AWS Cloud Engineer

This repository contains a comprehensive guide and necessary files to help you understand and implement various AWS services through the AWS CLI and Python SDK. The tasks are divided into two main sections: Block Storage and Object Storage. Each section includes detailed steps, commands, and scripts required to accomplish the tasks.

## Repository Contents

### Help Command Files

These files contain the help command outputs for various AWS services and commands:

- **command-aws.txt**: Help command for AWS CLI.
- **commands-aws-ec2.txt**: Help command for EC2 service.
- **commands-aws-ec2-run-instances.txt**: Help command for EC2's run-instances command.
- **commands-aws-iam.txt**: Help command for IAM service.
- **commands-aws-iam-get-policy.txt**: Help command for IAM's get-policy command.
- **commands-aws-iam-list-policies.txt**: Help command for IAM's list-policies command.
- **commands-aws-s3api.txt**: Help command for S3 API service.
- **commands-aws-s3api-create-bucket.txt**: Help command for S3 API's create-bucket command.

### Task Execution Files

- **Storage Tasks - all executed commands.txt**: Contains all the CLI commands executed to perform the tasks.
- **my-s3-python.py**: Python code to access a file in S3 storage using Flask.
- **my-s3-file.txt**: Text file used by the Python code.

### JSON Files for Resource Tagging and Policy

- **policy-s3.json**: JSON file to create an IAM policy.
- **tags-instance.json**: JSON file to create tags for EC2 instances.
- **tags-routetable.json**: JSON file to create tags for route tables.
- **tags-subnet.json**: JSON file to create tags for subnets.
- **tags-volume.json**: JSON file to create tags for volumes.
- **tags-vpc.json**: JSON file to create tags for VPCs.

### Documentation

- **Storage-Documentation.docx**: Documentation of all the commands executed and their screenshots.
- **Storage-Documentation.pdf**: PDF format of the documentation.

### RSA Key

- **Sample-key-pair.pem**: Sample RSA key for access to EC2 resources of AWS.

## Tasks Performed

### i. Block Storage

1. Download and install the AWS CLI.
2. Create a public subnet in a VPC.
3. Create an EC2 instance with a public IP address.
4. Check available storage types for block volumes.
5. Create a 10 GB block storage volume (Standard/Magnetic).
6. Attach the block storage volume to the EC2 instance.
7. Modify the volume to 25 GB or higher (SSD).
8. Attempt to delete the volume.
9. Delete the EC2 instance and any attached block storage volumes.
10. Document each step with screenshots and commands in `Storage-Documentation.docx`.

### ii. Object Storage

1. Create an IAM policy for object storage bucket management.
2. Create an object storage bucket.
3. List the created buckets.
4. Create a text file with "Hello Object Storage".
5. Copy the text file to the bucket.
6. List the objects in the bucket.
7. Create an EC2 instance.
8. Write a Python Flask program to read the text file from the bucket and return it in an HTTP response.
9. Delete the file, the bucket, and the EC2 instance.
10. Document each step with screenshots and commands in `Storage-Documentation.docx`.

## Requirements

### AWS CLI

To execute the commands provided in this repository, you need to have the AWS CLI installed and configured.

1. **Install AWS CLI**:
   Follow the installation guide from the [AWS CLI official documentation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
2. **Configure AWS CLI**:

   ```bash
   aws configure
   ```

   You will need to provide your AWS Access Key, Secret Key, default region, and output format.

### Python and Dependencies

To run the Python Flask application, you need to have Python and the required libraries installed.

1. **Install Python**:
   Ensure you have Python 3.6 or later installed. You can download it from the [official Python website](https://www.python.org/downloads/).
2. **Create a `requirements.txt` file with the following content**:
   ```text
   Flask
   boto3
   ```
3. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
4. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Roadmap-to-AWS-Cloud-Engineer.git
   cd Roadmap-to-AWS-Cloud-Engineer
   ```
2. **Execute the commands:**
   Follow the commands in `Storage Tasks - all executed commands.txt` to set up your AWS environment.
3. **Run the Python Flask app:**

   ```bash
   python my-s3-python.py
   ```
4. **View the Flask app:**
   Open your browser and navigate to `http://localhost:5000/hello` to see the content from the S3 bucket.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the AWS documentation and community for providing comprehensive guides and examples.

---

Feel free to explore the repository and use it as a guide to enhance your skills in managing AWS services through the CLI and Python SDK. If you have any questions or suggestions, please open an issue or submit a pull request.
