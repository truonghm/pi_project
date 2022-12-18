from __future__ import annotations
import unittest

from LegacyApp.Client import Client
from LegacyApp.ClientStatus import ClientStatus
from enum import auto

class TestClient(unittest.TestCase):
	def test_id_getter(self):
		client = Client(id = 1)
		self.assertEqual(client.id, 1)

	def test_id_setter(self):
		client = Client()
		client.id = 1
		self.assertEqual(client.id, 1)

	def test_name_getter(self):
		client = Client(name = 'Duck')
		self.assertEqual(client.name, 'Duck')

	def test_name_setter(self):
		client = Client()
		client.name = 'Duck'
		self.assertEqual(client.name, 'Duck')

	def test_status_getter(self):
		for status in ClientStatus:
			client = Client(status = eval(f"ClientStatus.{status.name}"))
			self.assertEqual(client.status, eval(f"ClientStatus.{status.name}"))

	def test_status_setter(self):
		for status in ClientStatus:
			client = Client()
			client.status = eval(f"ClientStatus.{status.name}")
			self.assertEqual(client.status, eval(f"ClientStatus.{status.name}"))