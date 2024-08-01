from django.core.exceptions import ValidationError
from django.utils.text import slugify



def validate_slugify(value):
    # if slugify version is different to value, there are something wrong, so raise error.
    if slugify(value) != value:
        raise  ValidationError("Please make sure slug is in lowercase")

    
