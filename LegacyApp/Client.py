from __future__ import annotations
from .ClientStatus import ClientStatus
from enum import auto

class Client:
    def __init__(self: Client, id: int = -1, name: str= '', status: auto = ClientStatus.UNDEFINED):
        self.__id = id
        self.__name = name
        self.__status = status

    @property
    def id(self: Client) -> int:
        return self.__id

    @id.setter
    def id(self: Client, id: int):
        self.__id = id

    @property
    def name(self: Client) -> str:
        return self.__name

    @name.setter
    def name(self: Client, name: str):
        self.__name = name

    @property
    def status(self: Client) -> auto:
        return self.__status

    @status.setter
    def status(self: Client, status: auto):
        self.__status = status
