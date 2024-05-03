
from typing import Iterable, Optional
from src.config.my_connexion import MyConnexion
from src.dao.generic_dao import GenericDao
from src.models.user import User


class UserDao (GenericDao[User]):
    __db = None

    def __init__(self) -> None:
        self.__db = MyConnexion()

    def save(self, user: User) -> User:
        query = 'insert into user (id,first_name,last_name,email,password) values(%s,%s,%s,%s,%s)'
        params = [user._id, user._first_name, user._last_name,
                  user._email, user._password]
        return self.__db.save(query, params)

    def update(self, user: User) -> User:
        pass

    def delete(self, user: User) -> None:
        pass

    def find_all(self) -> Iterable[User]:
        return self.__db.query('select * from user').fetchall()

    def find_by_id(self, id) -> Optional[User]:
        query = 'select * from user where id = %s'
        params = [id]
        return self.__db.query(query, params).fetchone()

    def find_by_email(self, email) -> User | None:
        query = 'select * from user where email = %s'
        params = [email]
        return self.__db.query(query, params).fetchone()

    def update_password(self, id, new_password) -> User | None:
        query = 'update user set password = %s   where id = %s '
        params = [new_password, id]
        return self.__db.update(query, params)
