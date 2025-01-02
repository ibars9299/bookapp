from django.core.exceptions import ValidationError
import magic
import os

def validate_file_type(file):
    # Dosya türü kontrolü
    allowed_types = ['application/pdf']
    file_type = magic.from_buffer(file.read(1024), mime=True)
    if file_type not in allowed_types:
        raise ValidationError('Sadece PDF dosyaları yüklenebilir.')

def validate_file_size(file):
    # Maksimum 50MB
    max_size = 50 * 1024 * 1024
    if file.size > max_size:
        raise ValidationError('Dosya boyutu 50MB\'dan büyük olamaz.') 