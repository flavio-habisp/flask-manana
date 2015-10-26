"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from flask.globals import current_app as app
import hashlib

from .models import User


def encript_password(email, password):
    hashable_str = '{email}.{password}.{salt}'.format(
        email=email,
        password=password,
        salt=app.config['SECRET_KEY']
    )
    return hashlib.sha512(hashable_str.encode('utf-8')).hexdigest()


def user_register(name, email, password):
    """ Register new user """
    user = User(
        name=name,
        email=email,
        password=encript_password(email, password),
    )
    return user.save()


def check_user_password(user, password):
    """ Checks the plaintext password against the user's encrypted Password."""
    return encript_password(user.email, password) == user.password
