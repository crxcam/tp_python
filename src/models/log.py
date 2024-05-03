

class Log:
    def __init__(self,
                 is_error: bool = False,
                 operation_name: str = '',
                 operation_date: str = '',
                 user_id: str = '',
                 error_content:str=''
                 ) -> None:
        self.__is_error = is_error
        self.__operation_name = operation_name
        self.__operation_date = operation_date
        self.__user_id = user_id
        self.__error_content = error_content

    @property
    def _is_error(self):
        return self.__is_error

    @_is_error.setter
    def _is_error(self, value):
        self.__is_error = value

    @property
    def _operation_name(self):
        return self.__operation_name

    @_operation_name.setter
    def _operation_name(self, value):
        self.__operation_name = value

    @property
    def _operation_date(self):
        return self.__operation_date

    @_operation_date.setter
    def _operation_date(self, value):
        self.__operation_date = value

    @property
    def _user_id(self):
        return self.__user_id

    @_user_id.setter
    def _user_id(self, value):
        self.__user_id = value

    @property
    def _error_content(self):
        return self.__error_content

    @_error_content.setter
    def _error_content(self, value):
        self.__error_content = value

