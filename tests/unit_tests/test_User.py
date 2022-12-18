from __future__ import annotations
import unittest

from LegacyApp.Client import Client
from LegacyApp.User import User
from datetime import datetime

class TestClient(unittest.TestCase):

    def setUp(self):
        client = Client(id=1)
        self.user = User(
            client=client,
            date_of_birth=datetime(year=1970, month=1, day=1),
            email_address='test_user@fakecompany.com',
            first_name='John',
            surname='Smith'
        )

    def test_client_getter(self):
        self.assertIsInstance(self.user.client, Client)

    def test_client_setter(self):
        new_client = Client(id=2)
        self.user.client = new_client
        self.assertIsInstance(self.user.client, Client)
        self.assertEqual(self.user.client.id, 2)

    def test_dob_getter(self):
        self.assertIsInstance(self.user.date_of_birth, datetime)
        self.assertEqual(self.user.date_of_birth, datetime(year=1970, month=1, day=1))

    def test_dob_setter(self):
        self.user.date_of_birth = datetime(year=1970, month=1, day=2)
        self.assertIsInstance(self.user.date_of_birth, datetime)
        self.assertEqual(self.user.date_of_birth, datetime(year=1970, month=1, day=2))

    def test_email_getter(self):
        self.assertEqual(self.user.email_address, 'test_user@fakecompany.com')

    def test_email_setter(self):
        self.user.email_address = 'test_user2@fakecompany.com'
        self.assertEqual(self.user.email_address, 'test_user2@fakecompany.com')

    def test_first_name_getter(self):
        self.assertEqual(self.user.first_name, 'John')

    def test_first_name_setter(self):
        self.user.first_name = 'Adam'
        self.assertEqual(self.user.first_name, 'Adam')

    def test_surname_getter(self):
        self.assertEqual(self.user.surname, 'Smith')

    def test_surname_setter(self):
        self.user.surname = 'Thomas'
        self.assertEqual(self.user.surname, 'Thomas')

    def test_has_credit_limit_getter(self):
        self.assertFalse(self.user.has_credit_limit)

    def test_has_credit_limit_setter(self):
        self.user.has_credit_limit = True
        self.assertTrue(self.user.has_credit_limit)

    def test_credit_limit_getter(self):
        self.assertEqual(self.user.credit_limit, -1)

    def test_credit_limit_setter(self):
        for i in range(990, 1001):
            self.user.credit_limit = i
            self.assertEqual(self.user.credit_limit, i)
