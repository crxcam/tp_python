from src.models.account import Account
from src.dao.account_dao import AccountDao
import uuid

account_dao = AccountDao()


def account_create_one(tup: tuple[int],
                       salt: str = '',
                       id_user: str = '',
                       ) -> None:
    account = Account(str(uuid.uuid4()), str(tup), salt, id_user)
    account_dao.save(account)


def find_by_user_id(id_user: str = '',
                    ) -> Account | None:
    account_tuple = account_dao.find_by_user_id(id_user)
    if account_tuple:
        return Account(account_tuple[0], tranform_string_to_tuple(account_tuple[3]), account_tuple[2], account_tuple[1])
    return None


def tranform_string_to_tuple(value: str) -> tuple[int]:
    x1 = value.replace("(", "")
    x2 = x1.replace(")", "")
    return tuple(map(int, x2.split(', ')))


def update_password_data(id: str = '', tup: tuple[int] = [], salt: str = '') -> Account | None:
    return account_dao.update_password_data(id, str(tup), salt)

def delete_account(id:str)-> None:
    account_dao.delete(id)
