import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x0e\x0fF\x18\xaarP\xd5\xb7U:e\xde\xbc\xa5\x80'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'} 
