
import datetime
from src.models.log import Log
from src.models.app_actions import AppActions


def save_log(is_error: bool = False,
             operation_name: AppActions = AppActions.USER_CREATE_ACCOUNT,
             user_id: str = '',
             error_content: str = '',
             ) -> None:
    save_log_in_file(Log(is_error, operation_name, str(
        datetime.datetime.now()), user_id, error_content))


def save_log_in_file(log: Log) -> None:
    txt_is_error: str = "## LOG ## => "
    if log._is_error:
        txt_is_error: str = "## ERROR ## => "
    msg: str = f"{txt_is_error} | user id [{log._user_id}] | operation : {
        log._operation_name} | date : {log._operation_date} | error : [{log._error_content}]  \n"

    logs_file = open('./logs.txt', 'a')
    logs_file.write(msg)
    logs_file.close()
