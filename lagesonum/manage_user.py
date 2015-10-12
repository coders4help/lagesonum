#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

import warnings
from optparse import Option, OptionParser
from sys import stdout, stderr
from warnings import warn
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from models import BaseModel, User
from getpass import getpass
from passlib.hash import sha256_crypt

_options = [
    Option('-d', '--database', help=u'Database file', action='store', type='string'),
    Option('-l', '--list', help=u'List all users (matching [arguments])', action='store_true'),
    Option('-a', '--add', help=u'Add user', action='store_true'),
    Option('-r', '--remove', help=u'Remove user', action='store_true'),
]

um = None


def print_user(user, file=stdout):
    print(u'User: ({:d}) {} [{}] {}'.format(user.id, user.username, r'********' if user.password else '-',
                                            'x' if user.is_admin else '-'), file=file)


def check_add_arguments(arguments):
    username = None
    password = None
    is_admin = False

    if len(arguments) > 2:
        username, password, is_admin = arguments
    elif len(arguments) > 1:
        username, password = arguments
    elif arguments:
        username = ''.join(arguments).strip()

    if not username:
        username = input(u'Username: ')

    if not password:
        password = getpass(u'Password: ')
        password2 = getpass(u'Password (repeat): ')
        if password != password2:
            print(file=stderr)
            print(u'Passwords didn\'t match', file=stderr)
            print(file=stderr)
            return None, None, None

    is_admin = is_admin and str(True).lower() == str(is_admin).lower()

    return username, password, is_admin


def list_users_matching(matches):
    for user in um.session.query(User).all():
        if not user:
            continue
        if not matches or 'all' == matches or user.username in matches:
            print_user(user)
        else:
            for match in matches:
                if user.username.startswith(match) or user.username.endswith(match):
                    print_user(user)


def add_user(arguments):
    username, password, is_admin = check_add_arguments(arguments)

    if username and password:
        password_hash = sha256_crypt.encrypt(password)
        try:
            u = User(username=username, password=password_hash, is_admin=is_admin)
            um.session.add(u)
            um.session.flush()
            print(u'Created user {} as {}admin'.format(u.username, u'non' if not u.is_admin else ''))
        except IntegrityError as e:
            warn(u'User seems to already exist: {}'.format(e))
    else:
        warn(u'Unable to create user. See previous output for potential reasons.')


def remove_user(usernames):
    users_query = um.session.query(User)

    unames = []
    if 'all' == usernames:
        pass
    elif isinstance(usernames, list):
        unames = usernames
    elif len(usernames) > 0:
        unames = [usernames]
    else:
        prompt = u'Username to delete (empty line to continue): '
        unames = []
        uname = input(prompt).strip()
        while uname:
            unames.append(uname)
            uname = input(prompt).strip()

        if not unames:
            warn(u'No usernames for deletion given')
            return

    if unames:
        users_query = users_query.filter(User.username.in_(unames))

    try:
        users = users_query.all()
        print(u'Delete users: {}'.format([u.username for u in users or []]), file=stderr)
        for user in users:
            um.session.delete(user)
        um.session.flush()
        count_query = um.session.query(func.count(User.username))
        if unames: count_query = count_query.filter(User.username.in_(unames))
        if count_query.one()[0] < len(users):
            print(u'Deleted {} users'.format(len(users) - count_query.one()[0]))
    except Exception as e:
        warn(u'Error deleting users: {}'.format(e))


class UserManager:
    def __init__(self, database, options):
        self.model = BaseModel(database=database)

        self.connect()

        local_opts =options.__dict__.copy()
        local_opts.pop('database')
        for option in local_opts:
            setattr(self, option, local_opts[option])

    def connect(self):
        self.session = self.model.create_session()

    def disconnect(self):
        self.commit()
        self.model.remove_session()
        self.session = None

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def run(self, arguments):
        self.connect()

        try:
            if self.list:
                list_users_matching(arguments)
            elif self.add:
                add_user(arguments)
            elif self.remove:
                remove_user(arguments)
            else:
                warn(u'No command given', UserWarning)

            self.commit()
        except Exception as e:
            self.rollback()
            raise RuntimeError from e
        finally:
            try:
                self.disconnect()
            except:
                pass


if __name__ == '__main__':
    _cmd_parser = OptionParser(usage=u'%prog [options] [arguments]', option_list=_options, add_help_option=True)
    _cmd_options, _cmd_args = _cmd_parser.parse_args()
    if not _cmd_options.database:
        _cmd_parser.print_help()
        exit(1)
    if not os.path.exists(_cmd_options.database):
        _cmd_parser.print_help()
        exit(2)

    um = UserManager(_cmd_options.database, _cmd_options)

    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter('always')
        um.run(_cmd_args)

    if len(warns) > 0:
        print(file=stderr)
        for w in warns:
            print(w.message, file=stderr)
        print(file=stderr)


# vim: ts=4:sts=4:sw=4:et:ai
