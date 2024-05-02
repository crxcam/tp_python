

class User:
    def __init__(self, id: str = '',
                 first_name: str = '',
                 last_name: str = '',
                 email: str = '',
                 last_password: str = '',
                 current_password: str = ''
                 ) -> None:
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__last_password = last_password
        self.__current_password = current_password

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
    def _last_password(self):
        return self.__last_password

    @_last_password.setter
    def _last_password(self, value):
        self.__last_password = value

    @property
    def _current_password(self):
        return self.__current_password

    @_current_password.setter
    def _current_password(self, value):
        self.__current_password = value



# cela permet d'afficher object dans print

    def __str__(self) -> str:
        return f' id:{self._num} nom:{self._nom} prenom:{self._prenom}'

    def __repr__(self) -> str:
        return f'{self.nom} {self.prenom} {self.age}'
