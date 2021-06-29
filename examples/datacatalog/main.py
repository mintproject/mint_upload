from minio import Minio
from minio.error import S3Error
from pathlib import Path
import os
import logging

def main():
    server = "dev.data.mint.isi.edu"
    username = "datacatalog"
    password = os.environ["PASSWORD"]
    bucket_name = 'gldas'

    client = Minio(
        server,
        access_key=username,
        secret_key=password
    )

    found = client.bucket_exists(bucket_name)
    if not found:
        logging.error("Bucket doesn't exists")
        exit(1) 

    objects = client.list_objects(bucket_name)
    for obj in objects:
        print(obj)


    file_path = Path('.') / "requirements.txt"
    result = client.fput_object(
        bucket_name, file_path.name, file_path,
    )
    location = f"""https://{server}/{bucket_name}/{result.object_name}"""
    print(location)

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        logging.error(exc)


