import unittest

from LegacyApp.UserService import UserService
from datetime import datetime


class TestClient(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()

    def tearDown(self):
        pass

    def test_invalid_first_name(self):
        add_result = self.user_service.add_user(
            "",
            "Sponge",
            "spongebob@spongemail.com",
            datetime(1969, 12, 4),
            3
        )
        self.assertFalse(add_result)

    def test_invalid_sir_name(self):
        add_result = self.user_service.add_user(
            "Bob",
            "",
            "spongebob@spongemail.com",
            datetime(1969, 12, 4),
            3
        )
        self.assertFalse(add_result)

    def test_invalid_email_case1(self):
        add_result = self.user_service.add_user(
            "Bob",
            "Sponge",
            "spongebob@spongemail",
            datetime(1969, 12, 4),
            3
        )
        self.assertFalse(add_result)

    def test_invalid_email_case2(self):
        add_result = self.user_service.add_user(
            "Bob",
            "Sponge",
            "spongebobspongemail.com",
            datetime(1969, 12, 4),
            3
        )
        self.assertFalse(add_result)

    def test_invalid_dob(self):
        add_result = self.user_service.add_user(
            "Bob",
            "Sponge",
            "spongebob@spongemail.com",
            datetime(2022, 12, 4),
            3
        )
        self.assertFalse(add_result)

    def test_valid_user(self):
        add_result = self.user_service.add_user(
            "Bob",
            "Sponge",
            "spongebob@spongemail.com",
            datetime(1969, 12, 4),
            3
        )
        self.assertTrue(add_result)
