import os

ENVIRONMENT = os.environ.get('DJANGO_SETTINGS_MODULE', '')

if ENVIRONMENT == 'tax_calculator_api.settings':
    from .develop import *
