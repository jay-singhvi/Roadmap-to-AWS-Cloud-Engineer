from flask import Flask, Response, jsonify
import boto3
from botocore.exceptions import (
    NoCredentialsError,
    PartialCredentialsError,
    TokenRetrievalError,
)

app = Flask(__name__)


def create_boto3_session(profile_name):
    try:
        session = boto3.Session(profile_name=profile_name)
        return session
    except TokenRetrievalError as e:
        print(f"Token retrieval error: {e}")
        print(
            f"Please run `aws sso login --profile {profile_name}` to renew your SSO token."
        )
        return None
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
        return None


def get_file_from_s3(bucket_name, file_name, profile_name):
    session = create_boto3_session(profile_name)
    if not session:
        return "AWS SSO token has expired or there is an issue with credentials."

    s3_client = session.client("s3", region_name="us-east-1")
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        return obj["Body"].read().decode("utf-8")
    except s3_client.exceptions.NoSuchKey:
        return "The specified key does not exist."
    except Exception as e:
        return f"Error retrieving file: {e}"


profile_name = "aws_admin_user1"
bucket_name = "my-object-storage-bucket"
file_name = "my-s3-file.txt"


@app.route("/hello")
def hello():
    return get_file_from_s3(bucket_name, file_name, profile_name)


if __name__ == "__main__":
    app.run(debug=True)
