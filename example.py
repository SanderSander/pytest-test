import os

APP_REDIS_HOST = os.environ.get('WERCKER_REDIS_HOST', '127.0.0.1')
APP_REDIS_PORT = os.environ.get('WERCKER_REDIS_PORT', '6379')
REDIS_HOST = os.environ.get('WERCKER_REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('WERCKER_REDIS_PORT', '6379')

