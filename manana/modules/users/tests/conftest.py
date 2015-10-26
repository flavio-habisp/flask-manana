"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
import pytest
from manana.modules.users.utils import user_register


@pytest.fixture(scope='session')
def user_demo(db):
    user = user_register(
        name='demo',
        password='demodemo',
        email='demo@example.com'
    )
    return user
