

class User:
    def __init__(self, 
                 id: str = '',
                 first_name: str = '',
                 last_name: str = '',
                 email: str = '',
                 password: str = ''
                 ) -> None:
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _first_name(self):
        return self.__first_name

    @_first_name.setter
    def _first_name(self, value):
        self.__first_name = value

    @property
    def _last_name(self):
        return self.__last_name

    @_last_name.setter
    def _last_name(self, value):
        self.__last_name = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _password(self):
        return self.__password

    @_password.setter
    def _password(self, value):
        self.__password = value


    def __str__(self) -> str:
        return f' id:{self._id} nom:{self._first_name} prenom:{self._last_name}'

    def __repr__(self) -> str:
         return f' id:{self._id} nom:{self._first_name} prenom:{self._last_name}'
