

from typing import Optional
from src.models.account import Account
from src.models.user import User
from src.dao.user_dao import UserDao

import src.tools.crypt_service as crypt_service
import src.tools.account_service as account_service

import uuid

user_dao = UserDao()

def build_auth_response(auth_is_valid: bool, user: Optional[User | None] = None) -> tuple[bool,str]:
    if auth_is_valid:
        return auth_is_valid, f"{user._first_name},{user._last_name},{user._email}"
    return False, 'Authentification incorrect'

def user_create_one(first_name: str = '',
                    last_name: str = '',
                    email: str = '',
                    clear_password: str = '') -> tuple[bool, str]:
    #   check mail exist
    user = user_dao.find_by_email(email)
    if user:
        return False, 'Mail existe déja'
    #   crypt password
    crypt_result: tuple[str, int] = crypt_service.crypt(clear_password)
    salt = crypt_result[0]
    key = crypt_result[1]
    passport_crypted = crypt_result[2]
    id_user: str = str(uuid.uuid4())

    #   save user
    user = User(id_user, first_name, last_name,
                email, passport_crypted)
    user_dao.save(user)
    #   save account
    account_service.account_create_one(key, salt, id_user)
    return (True, 'Utilisateur crée avec succès')

def user_login(email: str, input_pswd: str):
    tuple_user_account= build_user_and_account(email)
    if not tuple_user_account:
        return build_auth_response(False)
    user: User = tuple_user_account[0]
    account: Account = tuple_user_account[1]
    if not crypt_service.compare_password(input_pswd, account._salt, account._tup, user._password):
        return build_auth_response(False)
    return build_auth_response(True, user)

def replace_password(current_password:str,new_password:str,email:str)-> tuple[bool,str]:
    if current_password == new_password:
        return False, 'Le nouveau mot de passe doit être differente de mot de passe actuel!'
    tuple_user_account= build_user_and_account(email)
    user: User = tuple_user_account[0]
    account: Account = tuple_user_account[1]
    if not crypt_service.compare_password(current_password, account._salt, account._tup, user._password):
        return build_auth_response(False)
    # update password data 
    account_update_data = crypt_service.crypt(new_password)
    user_dao.update_password(user._id,account_update_data[2])
    account_service.update_password_data(account._id,account_update_data[1],account_update_data[0])
    return True, 'Le nouveau mot de passe enregistré avec succès!'

def build_user_and_account(email:str)-> Optional[tuple[User,Account]:None]:
    user_raw = user_dao.find_by_email(email)
    if not user_raw:
        return None
    user: User = User(user_raw[0], user_raw[1], user_raw[2],
                      user_raw[3], user_raw[4])
    account: Account = account_service.find_by_user_id(user._id)
    if not account:
        return None
    return user,account
    
