"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""

from manana.modules.users.models import User
from manana.modules.users.utils import check_user_password


def test_get_by_email(user_demo):
    assert user_demo == User.get_by_email(user_demo.email)


def test_get(user_demo):
    assert user_demo == User.get(user_demo.rn)


def test_check_user_password(user_demo):
    assert check_user_password(user_demo, 'demodemo')
