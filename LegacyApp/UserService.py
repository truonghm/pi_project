from __future__ import annotations
from datetime import datetime
from abc import ABC, abstractmethod

from .Client import IClient
from .ClientStatus import ClientStatus
from .ClientRepository import ClientRepository
from .User import User, IUser
from .UserCreditService import UserCreditServiceClient
from .UserDataAccess import UserDataAccess


class UserValidationError(Exception):
    pass


class UserInfoValidation:
    @staticmethod
    def validate_first_name(first_name: str) -> str:
        if first_name == "":
            raise UserValidationError("Input values for first name is not valid")

        return first_name

    @staticmethod
    def validate_last_name(last_name: str) -> str:
        if last_name == "":
            raise UserValidationError("Input values for last name is not valid")

        return last_name

    @staticmethod
    def validate_email(email: str) -> str:
        error_message = "Input value for email is not valid"
        if "@" not in email:
            raise UserValidationError(error_message)
        else:
            if "." not in email:
                raise UserValidationError(error_message)

        return email

    def validate_dob(date_of_birth: datetime) -> datetime:
        now = datetime.now()
        age = now.year - date_of_birth.year
        if (now.month < date_of_birth.month) or (
            (now.month == date_of_birth.month) and (now.day < date_of_birth.day)
        ):
            age = age - 1
        if age < 21:
            raise UserValidationError("Input value for date of birth is not valid")

        return date_of_birth

    def get_client(client_id: int) -> IClient:
        client_repository = ClientRepository()
        client = client_repository.get_by_id(client_id)

        return client

    @classmethod
    def validate(
        cls,
        firname: str,
        surname: str,
        email: str,
        dateOfBirth: datetime,
        clientId: int,
    ) -> IUser:
        first_name = cls.validate_first_name(firname)
        last_name = cls.validate_last_name(surname)
        email = cls.validate_email(email)
        date_of_birth = cls.validate_dob(dateOfBirth)
        client = cls.get_client(clientId)

        user = User(
            client=client,
            date_of_birth=date_of_birth,
            email_address=email,
            first_name=first_name,
            surname=last_name,
        )

        return user


class UserCreditLimitValidation:
    @staticmethod
    def validate(user: User) -> User:
        with UserCreditServiceClient() as user_credit_service:
            if user.client.status == ClientStatus.VIP:
                pass
            elif user.client.status == ClientStatus.IP:
                user.has_credit_limit = True
                user.credit_limit = (
                    user_credit_service.get_credit_limit(
                        user.first_name, user.surname, user.date_of_birth
                    ) * 2
                )
            else:
                user.has_credit_limit = True
                user.credit_limit = user_credit_service.get_credit_limit(
                    user.first_name, user.surname, user.date_of_birth
                )

        if user.has_credit_limit and (user.credit_limit < 500):
            raise ValueError("This user has invalid credit limit")

        return user


class IUserService(ABC):
    @staticmethod
    @abstractmethod
    def add_user(
        firname: str, surname: str, email: str, dateOfBirth: datetime, clientId: int
    ) -> bool:
        ...


class UserService(IUserService):

    # THIS METHOD SHOULD STAY STATIC, with same prototype...
    @staticmethod
    def add_user(
        firname: str, surname: str, email: str, dateOfBirth: datetime, clientId: int
    ) -> bool:
        # but you may add typing and you should modify its implementation...

        try:
            user = UserInfoValidation.validate(
                firname, surname, email, dateOfBirth, clientId
            )
            user = UserCreditLimitValidation.validate(user)
            UserDataAccess.add_user(user)
        except UserValidationError as e:
            # print(repr(e))
            return False

        return True
