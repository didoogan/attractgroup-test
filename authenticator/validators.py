from django.core.exceptions import ValidationError


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError("Only CSV file is accepted")
