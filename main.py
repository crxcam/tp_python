
from src.dao.user_dao import UserDao
from src.models.user import User
import src.tools.user_service as user_srv

dao = UserDao()
generic_error_response: str = "Une error est survenue pendant operation"


try:
    def user_create_one(first_name: str = '',
                        last_name: str = '',
                        email: str = '',
                        clear_password: str = '') -> str:
        response: tuple[bool, str] = user_srv.user_create_one(
            first_name, last_name, email, clear_password
        )
        print('User is created :', response[0])
        print('User is created message :', response[1])
except Exception as e:
    print(f"{generic_error_response}: ({e})")

try:
    def user_login(email: str, password: str) -> str:
        response: tuple[bool, str] = user_srv.user_login(
            email, password)
        print('User is loged :', response[0])
        print('User is loged message :', response[1])
except Exception as e:
    print(f"{generic_error_response}: ({e})")

try:
    def replace_password(current_password: str, new_password: str, email: str) -> str:
        response: tuple[bool, str] = user_srv.replace_password(
            current_password, new_password, email)
        print('User replace_password :', response[0])
        print('User replace_password message :', response[1])
except Exception as e:
    print(f"{generic_error_response}: ({e})")


#user_create_one('jonh', 'wick', 'toto2@gmail.com', 'password')
#user_login('toto2@gmail.com', 'password')
#replace_password('passwordff','password','toto2@gmail.com')
