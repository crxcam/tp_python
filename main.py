
#   models
from src.models.app_actions import AppActions
#   services
import src.tools.user_service as user_srv

response: tuple[bool, str] = ()

try:
    def user_create_one(first_name: str = '',
                        last_name: str = '',
                        email: str = '',
                        clear_password: str = '') -> str:
        response: tuple[bool, str] = user_srv.user_create_one(
            first_name, last_name, email, clear_password
        )
        print('User is created error :', response[0])
        print('User is created message :', response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_CREATE_ACCOUNT, str(e))

try:
    def user_login(email: str, password: str) -> str:
        response: tuple[bool, str] = user_srv.user_login(
            email, password)
        print('User is loged :', response[0])
        print('User is loged message :', response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_LOGIN, str(e))

try:
    def replace_password(current_password: str, new_password: str, email: str) -> str:
        response: tuple[bool, str] = user_srv.replace_password(
            current_password, new_password, email)
        print('User replace_password :', response[0])
        print('User replace_password message :', response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_CHANGE_PASSWORD, str(e))


try:
    def user_delete(email: str) -> str:
        response: tuple[bool, str] = user_srv.user_delete(email)
        print('User user_delete error :', response[0])
        print('User user_delete message :', response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_DELETE_ACCOUNT, str(e))

# user_create_one('jonh', 'wick', 'toto2@gmail.com', 'password')
# user_login('toto2@gmail.com', 'password')
# replace_password('passwordk','password','toto2@gmail.com')
# user_delete('toto2@gmail.com')

# log_srv.save_log(False, "test", "id user")
