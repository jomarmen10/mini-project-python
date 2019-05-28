import datetime

from peewee import *

DATABASE = SqliteDatabase('users.sqlite')

class User(Model):
    username = CharField()
    email = CharField()
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

