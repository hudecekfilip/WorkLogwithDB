import datetime

from peewee import *

db = SqliteDatabase('entries.db')

class Entry(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    username = CharField(max_length=80)
    date = DateTimeField()
    title = TextField()
    spent = IntegerField()
    note = TextField()


    class Meta:
        database = db


    def initialize(self):
        db.connect()
        db.create_tables([Entry], safe=True)
