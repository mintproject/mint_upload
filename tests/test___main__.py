"""Test the object storage
"""

from mint_upload.object_storage import  Uploader
import os

mint_auth_server = "https://auth.mint.mosorio.dev/auth/realms/development/protocol/openid-connect/token"
mint_s3_server = "https://s3.mint.mosorio.dev"
username = "demouser"
password = os.environ["PASSWORD"]
bucket_name = 'test'

def test_upload_file(tmp_path):
    """Check if we can upload a file

    Args:
        tmp_path ([type]): pytest temp path
    """
    uploader = Uploader(mint_s3_server, mint_auth_server, username, password)
    d = tmp_path / "sub"
    d.mkdir()
    p = d / 'hello.txt'
    p.write_text("context")
    uploader.upload_file(str(p), "test")

def test_get_cmd_line():
    uploader = Uploader(mint_s3_server, mint_auth_server, username, password)
    assert uploader.get_cmd_line()