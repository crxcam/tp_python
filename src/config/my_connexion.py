
import src.config.db_connexion_service as db_service
class  MyConnexion:

    __connexion = None
    __cursor = None

    def __init__(self) -> None:
        self.__connexion = db_service.get_mysql_db_connexion()
        self.__cursor = self.__connexion.cursor()

    def query(self,request,params:None=[]):
        self.__cursor.execute(request,params)
        return self.__cursor
    
    def save(self,request,params:None=[]):
        self.__cursor.execute(request,params)
        self.__connexion.commit()
        return self.__cursor
    
    def close(self):
        self.__cursor.close()
        self.__connexion.close()
