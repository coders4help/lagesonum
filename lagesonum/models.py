# coding: utf-8

from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Session = sessionmaker(autocommit=False)


class BaseModel():

    def __init__(self, database, **kwargs):
        super().__init__()
        self.engine = create_engine('sqlite:///{}'.format(database), echo=True)
        Base.metadata.create_all(self.engine)
        Session.configure(bind=self.engine)

    def create_session(self):
        return Session()


class User(Base, BaseModel):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(25), unique=True)
    password = Column('password', String(256))
    is_admin = Column('is_admin', Boolean, default=False)

    def __repr__(self):
        return u'User: {}, admin={}'.format(self.username, self.is_admin)


class Place(Base, BaseModel):
    __tablename__ = 'place'

    id = Column('id', Integer, primary_key=True)
    validation = Column('valregexp', String(99))
    name = Column('place', String(20), index=True)

    def __repr__(self):
        return u'Place: {} ({})'.format(self.name, self.validation)


class Number(Base, BaseModel):
    __tablename__ = 'number'

    id = Column('id', Integer, primary_key=True)
    number = Column('number', String(30))
    timestamp = Column('time', DateTime, default=datetime.now())
    user_id = Column('user_id', ForeignKey('user.id'))
    place_id = Column('place_id', ForeignKey('place.id'))
    fingerprint = Column('fingerprint', String(32))
    UniqueConstraint('number', 'fingerprint', name='number_fingerprint')

    user = relationship('User')
    place = relationship('Place')

    def __repr__(self):
        return u'Number: {} ({})'.format(self.number, self.timestamp, self.user)
