

class Account:
    def __init__(self,
                 id: str = '',
                 tup: str = '',
                 salt: str = '',
                 id_user: str = '',
                 ) -> None:
        self.__id = id
        self.__tup = tup
        self.__salt = salt
        self.__id_user = id_user

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _tup(self):
        return self.__tup

    @_tup.setter
    def _tup(self, value):
        self.__tup = value

    @property
    def _salt(self):
        return self.__salt

    @_salt.setter
    def _salt(self, value):
        self.__salt = value

    @property
    def _id_user(self):
        return self.__id_user

    @_id_user.setter
    def _id_user(self, value):
        self.__id_user = value


    def __str__(self) -> str:
        return f' id:{self._id}'

    def __repr__(self) -> str:
        return f' id:{self._id}'
