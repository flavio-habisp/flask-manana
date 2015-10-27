"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
import sys
import mongoengine

from manana.modules.mongodb import db
from manana.modules.mongodb.models import BaseMixin


ROOT_CATEGORY_RN = sys.maxsize


class ProductAttr(db.EmbeddedDocument):
    code = db.StringField()
    title = db.StringField()
    order_num = db.IntField(default=10)
    is_multiple = db.BooleanField(default=False)


class Category(BaseMixin):
    meta = {
        'indexes': ['rn', 'title', 'children']
    }
    rn = db.SequenceField(required=True, unique=True)
    parent = db.ReferenceField('self', reverse_delete_rule=mongoengine.CASCADE)
    path = db.ListField(db.IntField(), default=list)
    children = db.ListField(db.IntField(), default=list)
    title = db.StringField(required=True, max_length=255)
    order_num = db.IntField(required=True, default=100)
    enabled = db.BooleanField(default=True)
    product_attribute = db.ListField(db.EmbeddedDocumentField(ProductAttr))
    tech = db.DictField(default=dict)

    @property
    def has_children(self):
        return len(self.children) > 0 or self.is_root

    @property
    def is_root(self):
        return self.rn == ROOT_CATEGORY_RN
