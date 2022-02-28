from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 104857600:
        raise ValidationError("The maximum file size that can be uploaded is 100MB")
    else:
        return value
