

from enum import Enum


class AppActions(Enum):
    USER_CREATE_ACCOUNT = "Création d'un utilisateur"
    USER_LOGIN = "Connexion d'un utilisateur"
    USER_DELETE_ACCOUNT = "Supression d'un utilisateur"
    USER_CHANGE_PASSWORD = "Changement de mot de passe d'un utilisateur"
