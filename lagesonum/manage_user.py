#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

import warnings
from optparse import Option, OptionParser
from sys import stdout, stderr
from warnings import warn
from peewee import IntegrityError
from models import BaseModel, User
from passlib.hash import sha256_crypt

_options = [
    Option('-d', '--database', help=u'Database file', action='store', type='string'),
    Option('-l', '--list', help=u'List all users (matching [arguments])', action='store_true'),
    Option('-a', '--add', help=u'Add user', action='store_true'),
    Option('-r', '--remove', help=u'Remove user', action='store_true'),
]


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
        password = input(u'Password: ')
        password2 = input(u'Password (repeat): ')
        if password != password2:
            print(file=stderr)
            print(u'Passwords didn\'t match', file=stderr)
            print(file=stderr)
            return None, None, None

    is_admin = is_admin and str(True).lower() == str(is_admin).lower()

    return username, password, is_admin


def list_users_matching(matches):
    for user in User.select():
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
            u = User.create(username=username, password=password_hash, is_admin=is_admin)
            print(u'Created user {} as {}admin'.format(u.username, u'non' if not u.is_admin else ''))
        except IntegrityError as e:
            warn(u'User seems to already exist: {}'.format(e))
    else:
        warn(u'Unable to create user. See previous output for potential reasons.')


def remove_user(usernames):
    users = User.delete()

    if 'all' == usernames:
        pass
    elif len(usernames) > 0:
        users = users.where(User.username << usernames)
    else:
        prompt = u'Username to delete (empty line to continue): '
        unames = []
        uname = input(prompt).strip()
        while uname:
            unames.append(uname)
            uname = input(prompt).strip()
        if len(unames) > 0:
            users = users.where(User.username << unames)

    try:
        result = users.execute()
        print(u'Deleted {} users'.format(result), file=stderr)
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
        self.model.autocommit = False
        self.model.connect()

    def disconnect(self):
        self.model.disconnect()

    def commit(self):
        self.model.database.commit()

    def rollback(self):
        self.model.database.rollback()

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
