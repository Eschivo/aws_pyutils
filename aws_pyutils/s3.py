import boto3

def upload_file_using_client(bucket_name: str,
                             fpath: str,
                             object_name: str,
                             aws_profile: str = 'default') -> None:
    """
    Uploads file to S3 bucket using S3 client object
    :return: None
    """
    # setting up default profile for session
    boto3.setup_default_session(profile_name=aws_profile) # 
    s3 = boto3.client("s3")

    response = s3.upload_file(fpath, bucket_name, object_name)
    return response


def download_file_using_client(bucket_name: str,
                               object_name: str, 
                               fpath_dst: str, 
                               aws_profile: str = 'default') -> None:
    
    """
    Download file from S3 bucket using S3 client object

    ### Parameters
    bucket_name: str,
        The name of the bucket from which you want to download the file object
    object_name: str,
        The name of the object in the bucket you want to download
    fpath_dst: str,
        The full path to destination file on the local machine
    
    ### Return:
    None
    """

    boto3.setup_default_session(profile_name=aws_profile) # 
    s3 = boto3.client("s3")
    response = s3.download_file(bucket_name, object_name, fpath_dst)

    return response
