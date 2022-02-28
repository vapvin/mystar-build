import os
from django.conf import settings
from tempfile import SpooledTemporaryFile
from storages.backends.s3boto3 import S3Boto3Storage


class CustomS3Boto3Storage(S3Boto3Storage):
    def _save(self, name, content):
        content.seek(0, os.SEEK_SET)
        with SpooledTemporaryFile() as content_autoclose:
            content_autoclose.write(content.read())
            return super(CustomS3Boto3Storage, self)._save(name, content_autoclose)