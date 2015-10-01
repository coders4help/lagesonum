# coding: utf-8

from datetime import datetime
from peewee import *

database = SqliteDatabase(None)


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'database' in kwargs:
            database.init(database=kwargs['database'])
            self.connect()
            User.create_table(fail_silently=True)
            Place.create_table(fail_silently=True)
            Number.create_table(fail_silently=True)

    def connect(self):
        if database.is_closed():
            database.connect()

    def disconnect(self):
        if not database.is_closed():
            database.close()

    class Meta:
        database = database


class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField(unique=True, max_length=10)
    password = CharField(max_length=20)
    is_admin = BooleanField(default=False)

    @classmethod
    def create_table(cls, fail_silently=False):
        super().create_table(fail_silently)
        # if not User.select(User.username == 'admin').exists():
        #     User.create(username='admin', password='nimda')


class Place(BaseModel):
    id = PrimaryKeyField()
    valregexp = CharField(max_length=99, default=None)
    place = CharField(max_length=20)
    min_length = IntegerField(default=0)
    max_length = IntegerField(default=10)

    @classmethod
    def create_table(cls, fail_silently=False):
        super().create_table(fail_silently)
        if not Place.select(Place.place == 'LAGESO').exists():
            Place.create(place='LAGESO', valregexp=r'\b[a-z0-9]{4}\b')


class Number(BaseModel):
    id = PrimaryKeyField()
    number = CharField(max_length=30, null=False)
    time = DateTimeField(default=datetime.now)
    user = ForeignKeyField(User, null=True)
    place = ForeignKeyField(Place)
    fingerprint = CharField(max_length=32)

    class Meta:
        indexes = (
            (('number', 'fingerprint'), True),
        )
