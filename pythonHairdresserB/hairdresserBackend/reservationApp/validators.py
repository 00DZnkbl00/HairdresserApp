from django.core.exceptions import ValidationError
from datetime import time


def validate_time_interval(value):
    if value.minute % 30 != 0:
        raise ValidationError("Czas musi być w odstępach co 30 minut.")
