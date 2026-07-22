import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

chemin_db = os.path.join(BASE_DIR, "bibliotheque.db")

conn = sqlite3.connect(chemin_db)

class Livre:
    def __init__(self,titre,auteur,statut,genre,note):
        self.titre=titre
        self.auteur=auteur
        self.statut=statut
        self.genre=genre
        self.note=note

c = conn.cursor()


c.execute("""
          CREATE TABLE IF NOT EXISTS bibliotheque (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          titre TEXT,
          auteur TEXT,
          statut TEXT,
          genre TEXT,
          note REAL
          )
          """)

def ajouter_livre(titre,auteur,statut,genre,note):
    c.execute(
        """
        INSERT INTO bibliotheque
        (titre,auteur,statut,genre,note)
        VALUES(?,?,?,?,?)
        """,
        (titre,auteur,statut,genre,note)
    )
    conn.commit()

def supprimer_livre(ID):
    c.execute(
    """
    DELETE FROM bibliotheque WHERE id=?
    """,
    (ID,)
    )
    conn.commit()

def afficher_livre():
    c.execute("SELECT * FROM bibliotheque")
    livres=c.fetchall()
    return livres


def modifier_livre(id,titre,auteur,statut,genre,note):
    c.execute("""UPDATE bibliotheque 
              SET
                titre = ?,
                auteur = ?,
                statut = ?,
                genre=?,
                note = ?
              WHERE id = ?
              """,
              (titre,auteur,statut,genre,note,id)
    )
    conn.commit()

#########################

def selectionner_livre(id):
    c.execute(
        """SELECT * FROM bibliotheque WHERE id = ?""",
        (id,)
        )
    return c.fetchone()

def rechercher_livre(id):
    c.execute(
    """
    SELECT * FROM bibliotheque WHERE id= ?
""",
(id,)
)
    return c.fetchone

def vider_bibliotheque():
    c.execute("DELETE FROM bibliotheque")
    conn.commit()

conn.commit()
