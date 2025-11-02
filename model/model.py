from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self._cnx = get_connection()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:

        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        if self._cnx is None:
            print("Connessione al DB non valida")
            return []
        try:
            cursor = self._cnx.cursor()
            query = """SELECT * FROM automobile"""
            cursor.execute(query)
            righe = cursor.fetchall()
            lista_auto = []
            for row in righe:
                lista_auto.append(Automobile(row[0], row[1], row[2], row[3], row[4]))
            cursor.close()
            return lista_auto
        except Exception as e:
            print("Errore durante la lettura", e)
            return []


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        cursor = self._cnx.cursor()
        query = """SELECT * FROM automobile WHERE modello = %s"""
        cursor.execute(query, (modello,))
        righe = cursor.fetchall()
        lista_auto = []
        for row in righe:
            lista_auto.append(Automobile(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        return lista_auto
