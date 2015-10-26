"""
    :copyright: (c) 2015 by Vitaliy Kolesov, kvs1904+github@gmail.com.
    :license: GPLv3, see LICENSE for more details.
"""
from datetime import datetime
from manana.modules.mongodb import db


class BaseMixin(db.Document):
    meta = {'abstract': True, }
    rn = db.SequenceField(required=True)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def get_id(self):
        return self.rn

    @classmethod
    def get(cls, rn):
            return cls.objects(rn=rn).first()
