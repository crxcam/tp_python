
from src.dao.user_dao import UserDao
from src.models.user import User
import src.tools.user_service as user_srv

dao = UserDao()


def get_all():
    personnes = dao.find_all()
    print("get_all :")
    for personne in personnes:
        print(personne)


def get_one():
    personne = dao.find_by_id(1)
    print("get_one :", personne)



def user_create_one()->str:
    user_is_created:tuple[bool,str] = user_srv.user_create_one('jonh','wick','toto@gmail.com','password')
    print('User is created :',user_is_created[0])
    print('User is created message :',user_is_created[1])

user_create_one()


# get_all()
# get_one()
