"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""

from flask_login import UserMixin

from manana.modules.mongodb import db
from manana.modules.mongodb.models import BaseMixin


class Address(db.EmbeddedDocument):
    name = db.StringField(max_length=50, required=True)
    address1 = db.StringField(max_length=50, required=True)
    address2 = db.StringField(max_length=50)
    city = db.StringField(max_length=50, required=True)
    state = db.StringField(max_length=50, required=True)
    zip = db.StringField(max_length=50, required=True)
    country = db.StringField(max_length=50, required=True)
    phone = db.StringField(max_length=20)
    is_primary = db.BooleanField(default=False)


class User(BaseMixin, UserMixin):
    meta = {
        'indexes': ['email', 'name']
    }
    rn = db.SequenceField(collection_name='user')
    name = db.StringField(required=True, max_length=50)
    email = db.StringField(unique=True, max_length=255, required=True)
    password = db.StringField(required=True, max_length=255)
    addresses = db.ListField(db.EmbeddedDocumentField(Address))

    @classmethod
    def get_by_email(cls, email):
        """Fetch the User by email"""
        return User.objects(email=email).first()

    def get_id(self):
        """Method is the requirement of `UserMixin` class."""
        return self.rn
