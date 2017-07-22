import unittest

from flask import current_app
from app import create_app
from app.extensions import db
from app.modules.auth.models import User, Device
from app.modules.auth.schemas import UserSchema
from datetime import datetime, timedelta


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """test the application is existing"""
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """test the appliction running with TEST config"""
        self.assertTrue(current_app.config['TESTING'])

    def test_user_add(self):
        user = User(username = 'ok')
        user.hash_password('123456')
        db.session.add(user)
        db.session.commit()
        user1  = User.query.filter_by(username = 'ok').first()
        print (UserSchema().dump(user1).data)
        self.assertIsNotNone(user1)
        self.assertEqual(user.username, user1.username)

    def test_device(self):
        dev = Device(id = 1, user = 'ok11', expire_time=datetime.utcnow()+timedelta(days=1))
        db.session.add(dev)
        db.session.commit()
        self.assertTrue(Device.is_valid_device(1, 'ok11'))
        self.assertFalse(Device.is_valid_device(2, 'ok11'))
        self.assertFalse(Device.is_valid_device(1, 'nok'))

    def test_device_expired(self):
        dev = Device(id = 2, user = 'ok11', expire_time=datetime.utcnow()+timedelta(days=-1))
        db.session.add(dev)
        db.session.commit()
        self.assertFalse(Device.is_valid_device(2, 'ok11'))