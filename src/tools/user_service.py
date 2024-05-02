

from src.models.user import User
from src.dao.user_dao import UserDao
import uuid
user_dao = UserDao()


def user_create_one(first_name: str = '',
                    last_name: str = '',
                    email: str = '',
                    clear_password: str = '') -> tuple[bool, str]:

    print('user_service.user_create_one ')
    mail_exist = user_dao.email_exist(email)
    if mail_exist:
        return False, 'Mail existe déja'
    # hash password

    user_id: str = uuid.uuid4()
    user = User(user_id, 'first_name', 'last_name',
                'toto@gmail.com', 'last_password', 'current_password')
    # user_dao.save(user)
