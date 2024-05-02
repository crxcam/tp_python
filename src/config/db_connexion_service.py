
# necessite driver mysql
import mysql.connector
import json

configuration_file_path = "src/config/db_connexion.json"


def get_mysql_db_connexion():
    try:
        config_json = open(configuration_file_path)
        return mysql.connector.connect(**json.load(config_json))
    except  :
        print("get_mysql_db_connexion error ")
    finally:
        config_json.close()




def get_all(connexion):
    query = 'select * from  personne '
    curseur = connexion.cursor()
    curseur.execute(query)
    return curseur.fetchall()


def insert_one(nom: str, prenom: str, connexion):
    query = 'insert into personne (nom,prenom) values(%s,%s)'
    params = [nom, prenom]
    curseur = connexion.cursor()
    curseur.execute(query, params)
    connexion.commit()
