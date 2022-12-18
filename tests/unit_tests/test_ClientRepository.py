from __future__ import annotations
import unittest

from LegacyApp.Client import Client
from LegacyApp.ClientRepository import ClientRepository
from LegacyApp.ClientStatus import ClientStatus
from enum import auto

class TestClientRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.client_list = {
            1: ["Hugo Lasticot", ClientStatus.VIP],
            2: ["Madeleine Proust", ClientStatus.IP],
            3: ["Huguette Ponsif", ClientStatus.NORMAL],
            4: ["Georges Amphitryon", ClientStatus.VIP],
            5: ["Anibal Dupont", ClientStatus.IP],
            7: ["Georina Dupond", ClientStatus.NORMAL],
            8: ["Victor Elysea", ClientStatus.IP],
            9: ["Céline Quiboit", ClientStatus.NORMAL],
            10: ["Muriel Labeille", ClientStatus.NORMAL]
        }

        self.client_repository = ClientRepository()

    def test_get_by_id(self):
        for k, v in self.client_list.items():
            client_repository = ClientRepository()
            client = client_repository.get_by_id(k)
            self.assertEqual(v[0], client.name)
            self.assertEqual(v[1], client.status)

    def test_get_by_wrong_id(self):
        with self.assertRaises(Exception):
            client = self.client_repository.get_by_id(100)
