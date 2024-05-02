

from src.models.user import User
from src.dao.user_dao import UserDao

import src.tools.crypt_service as crypt_service
import src.tools.account_service as account_service

import uuid

user_dao = UserDao()


def user_create_one(first_name: str = '',
                    last_name: str = '',
                    email: str = '',
                    clear_password: str = '') -> tuple[bool, str]:
    #   check mail exist
    mail_exist = user_dao.email_exist(email)
    if mail_exist:
        return False, 'Mail existe déja'
    #   crypt password
    crypt_result: tuple[str, int] = crypt_service.crypt(clear_password)
    salt = crypt_result[0]
    key = crypt_result[1]
    passport_crypted = crypt_result[2]
    id_user: str = str(uuid.uuid4())

    #   save user
    user = User(id_user, first_name, last_name,
                email, passport_crypted, passport_crypted)
    user_dao.save(user)
    #   save account
    account_service.account_create_one(key, salt, id_user)
    return (True, 'Utilisateur crée avec succès')
