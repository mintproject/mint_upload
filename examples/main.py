from pathlib import Path
import logging
import os
from socket import error
from mint_upload.object_storage import Uploader

def main():
    mint_auth_server = "https://auth.mint.mosorio.dev/auth/realms/development/protocol/openid-connect/token"
    mint_s3_server = "https://s3.mint.mosorio.dev"
    username = "mosorio@isi.edu"
    password = os.environ["PASSWORD"]
    bucket_name = 'components'
    uploader = Uploader(mint_s3_server, mint_auth_server, username, password)
    file_path = Path('.') / "requirements.txt"
    try:
        uploader.upload_file(
            str(file_path),
            bucket_name
        )
    except Exception as error:
        raise error

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logging.error(error)


