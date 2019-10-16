import os

class Production(Config):
    SECRET_KEY = '\xa6\xbaG\x80\xc9-$s\xd5~\x031N\x8f\xd9/\x88\xd0\xba#B\x9c\xcd_'
    DEBUG = False
    DB_HOST = 'localhost'
    DB_USER = 'grupo36'
    DB_PASS = 'ZjVmMDRmZTczOTQ4'
    DB_NAME = 'grupo36'

class Development(Config):
    SECRET_KEY = "dev"
    DEBUG = True
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = ''
    DB_NAME = 'grupo36'