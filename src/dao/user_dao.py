
from typing import Iterable, Optional
from src.config.my_connexion import MyConnexion
from src.dao.generic_dao import GenericDao
from src.models.user import User


class UserDao (GenericDao[User]):
    __db = None

    def __init__(self) -> None:
        self.__db = MyConnexion()

    def save(self, user: User) -> User:
        query = 'insert into user (id,first_name,last_name,email,last_password,current_password) values(%s,%s,%s,%s,%s,%s)'
        params = [user._id, user._first_name,user._last_name,user._email,user._last_password,user._current_password]
        return self.__db.save(query,params)


    def update(self, user: User) -> User:
        pass

    def delete(self, user: User) -> None:
        pass

    def find_all(self) -> Iterable[User]:
        return self.__db.query('select * from user').fetchall()

    def find_by_id(self, id) -> Optional[User]:
        query = 'select * from user where id = %s'
        params=[id]
        return self.__db.query(query,params).fetchone()
    

    def email_exist(self, email) -> bool:
        query = 'select * from user where email = %s'
        params=[email]
        user = self.__db.query(query,params).fetchone()
        return user is not None