from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

DATABASES = get_secret("DATABASES")
