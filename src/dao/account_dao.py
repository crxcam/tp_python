
from src.config.my_connexion import MyConnexion
from src.dao.generic_dao import GenericDao
from src.models.account import Account


class AccountDao (GenericDao[Account]):
    __db = None

    def __init__(self) -> None:
        self.__db = MyConnexion()

    def save(self, account: Account) -> Account:
        query = 'insert into account (id,tup,salt,id_user) values(%s,%s,%s,%s)'
        params = [account._id, account._tup, account._salt, account._id_user]
        return self.__db.save(query, params)
