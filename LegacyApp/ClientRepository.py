from __future__ import annotations
from DB import DBAccess, DBTable
from typing import Type
from .Client import Client, IClient
from .ClientStatus import ClientStatus
from .tools import static_initializer


@static_initializer
class ClientRepository:
    __client_list = [
        (1, ["Hugo Lasticot", ClientStatus.VIP]),
        (2, ["Madeleine Proust", ClientStatus.IP]),
        (3, ["Huguette Ponsif", ClientStatus.NORMAL]),
        (4, ["Georges Amphitryon", ClientStatus.VIP]),
        (5, ["Anibal Dupont", ClientStatus.IP]),
        (7, ["Georina Dupond", ClientStatus.NORMAL]),
        (8, ["Victor Elysea", ClientStatus.IP]),
        (9, ["Céline Quiboit", ClientStatus.NORMAL]),
        (10, ["Muriel Labeille", ClientStatus.NORMAL])
    ]
    __table_name = 'clients'
    __table_description = ['name', 'status']
    __table_datatypes = [str, ClientStatus]

    @classmethod
    def static_init(cls: Type[ClientRepository]):
        cls.__clients = DBAccess.add_table(cls.__table_name, cls.__table_description, cls.__table_datatypes)
        for client in cls.__client_list:
            cls.__clients.add_entry(*client)
        # cls.__clients.add_entry(1, ["Hugo Lasticot", ClientStatus.VIP])
        # cls.__clients.add_entry(2, ["Madeleine Proust", ClientStatus.IP])
        # cls.__clients.add_entry(3, ["Huguette Ponsif", ClientStatus.NORMAL])
        # cls.__clients.add_entry(4, ["Georges Amphitryon", ClientStatus.VIP])
        # cls.__clients.add_entry(5, ["Anibal Dupont", ClientStatus.IP])
        # cls.__clients.add_entry(7, ["Georina Dupond", ClientStatus.NORMAL])
        # cls.__clients.add_entry(8, ["Victor Elysea", ClientStatus.IP])
        # cls.__clients.add_entry(9, ["Céline Quiboit", ClientStatus.NORMAL])
        # cls.__clients.add_entry(10, ["Muriel Labeille", ClientStatus.NORMAL])

    @classmethod
    def get_by_id(cls: Type[ClientRepository], id: int) -> IClient:
        entry = cls.__clients.get_entry(id)
        return Client(id, entry.get_value_by_column('name'), entry.get_value_by_column('status'))
