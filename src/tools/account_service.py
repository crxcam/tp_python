from src.models.account import Account
from src.dao.account_dao import AccountDao
import uuid

account_dao = AccountDao()

def account_create_one(tup: tuple[int],
                       salt: str = '',
                       id_user: str = '',
                       ) -> None:
    account = Account(str(uuid.uuid4()),str(tup) , salt, id_user)
    account_dao.save(account)

