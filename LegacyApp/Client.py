from __future__ import annotations
from .ClientStatus import ClientStatus
from abc import ABC, abstractmethod

class IClient(ABC):
    @property
    @abstractmethod
    def id(self: IClient) -> int: ...

    @property
    @abstractmethod
    def name(self: IClient) -> str: ...

    @property
    @abstractmethod
    def status(self: IClient) -> ClientStatus: ...


class Client(IClient):
    def __init__(self: Client, id: int = -1, name: str = '', status: ClientStatus = ClientStatus.UNDEFINED):
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
    def status(self: Client) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self: Client, status: ClientStatus):
        self.__status = status
