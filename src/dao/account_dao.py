
from typing import Optional
from src.config.my_connexion import MyConnexion
from src.dao.generic_dao import GenericDao
from src.models.account import Account


class AccountDao (GenericDao[Account]):
    __db = None

    def __init__(self) -> None:
        self.__db = MyConnexion()

    def save(self, account: Account) -> None:
        query = 'insert into account (id,tup,salt,id_user) values(%s,%s,%s,%s)'
        params = [account._id, account._tup, account._salt, account._id_user]
        self.__db.save(query, params)

    def find_by_user_id(self, id) -> Account | None:
        query = 'select * from account where id_user = %s'
        params = [id]
        return self.__db.query(query, params).fetchone()

    def update_password_data(self, id, tup, salt) -> Account | None:
        query = 'update account set tup = %s,salt =  %s  where id = %s '
        params = [tup, salt, id]
        return self.__db.update(query, params)
    
    def delete(self, id:str) -> None:
        query = 'delete  from account where id = %s'
        params = [id]
        return self.__db.delete(query, params).fetchone()
    
