# coding: utf-8

from datetime import datetime
from peewee import *


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'database' in kwargs:
            self._meta.database.init(database=kwargs['database'])
            self.connect()
            User.create_table(fail_silently=True)
            Place.create_table(fail_silently=True)
            Number.create_table(fail_silently=True)

    def connect(self):
        if self._meta.database.is_closed():
            self._meta.database.connect()

    def disconnect(self):
        if not self._meta.database.is_closed():
            self._meta.database.close()

    def commit(self):
        self._meta.database.commit()

    def rollback(self):
        self._meta.database.rollback()

    @property
    def autocommit(self):
        return self._meta.database.autocommit

    @autocommit.setter
    def autocommit(self, autocommit):
        self._meta.database.autocommit = autocommit

    class Meta:
        database = SqliteDatabase(None)


class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField(unique=True, max_length=10)
    password = CharField(max_length=256)
    is_admin = BooleanField(default=False)

    @classmethod
    def create_table(cls, fail_silently=False):
        super().create_table(fail_silently)


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
