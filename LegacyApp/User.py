from __future__ import annotations
from abc import ABC, abstractmethod
from .Client import IClient
from datetime import datetime


class IUser(ABC):
    @property
    @abstractmethod
    def client(self: IUser) -> IClient:
        ...

    @property
    @abstractmethod
    def date_of_birth(self: IUser) -> datetime:
        ...

    @property
    @abstractmethod
    def email_address(self: IUser) -> str:
        ...

    @property
    @abstractmethod
    def first_name(self: IUser) -> str:
        ...

    @property
    @abstractmethod
    def surname(self: IUser) -> str:
        ...

    @property
    @abstractmethod
    def has_credit_limit(self: IUser) -> bool:
        ...

    @property
    @abstractmethod
    def credit_limit(self: IUser) -> int:
        ...


class User(IUser):
    def __init__(
        self: User,
        client: IClient,
        date_of_birth: datetime,
        email_address: str,
        first_name: str,
        surname: str,
    ):
        self.__client = client
        self.__date_of_birth = date_of_birth
        self.__email_address = email_address
        self.__first_name = first_name
        self.__surname = surname
        self.__has_credit_limit = False
        self.__credit_limit = -1

    @property
    def client(self: User) -> IClient:
        return self.__client

    @client.setter
    def client(self: User, client: IClient):
        self.__client = client

    @property
    def date_of_birth(self: User) -> datetime:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self: User, date_of_birth: datetime):
        self.__date_of_birth = date_of_birth

    @property
    def email_address(self: User) -> str:
        return self.__email_address

    @email_address.setter
    def email_address(self: User, email_address: str):
        self.__email_address = email_address

    @property
    def first_name(self: User) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self: User, first_name: str):
        self.__first_name = first_name

    @property
    def surname(self: User) -> str:
        return self.__surname

    @surname.setter
    def surname(self: User, surname: str):
        self.__surname = surname

    @property
    def has_credit_limit(self: User) -> bool:
        return self.__has_credit_limit

    @has_credit_limit.setter
    def has_credit_limit(self: User, has_credit_limit: bool):
        self.__has_credit_limit = has_credit_limit

    @property
    def credit_limit(self: User) -> int:
        return self.__credit_limit

    @credit_limit.setter
    def credit_limit(self: User, credit_limit: int):
        self.__credit_limit = credit_limit
