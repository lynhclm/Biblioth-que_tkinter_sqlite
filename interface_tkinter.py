import tkinter as tk
from tkinter import ttk

from main import ajouter_livre, afficher_livre, modifier_livre,supprimer_livre

fenetre=tk.Tk()
fenetre.title("Gestionnaire lecture")
fenetre.geometry("800x750")
fenetre.config(bg="#E6D3FF")

titre = tk.Label(
    fenetre,
    text="Bibliothèque livres",
    font=("Arial", 20),
    bg=("#E6D3FF"),
    pady=30,
    fg="#F786FF"
)
titre.pack()

label_titre=tk.Label(fenetre, text="Titre", fg="#F786FF", bg="#E6D3FF", pady=10)
label_titre.pack()

entree_titre=tk.Entry(fenetre)
entree_titre.pack()


label_auteur=tk.Label(fenetre, text="Auteur", fg="#F786FF", bg="#E6D3FF", pady=10)
label_auteur.pack()

entree_auteur=tk.Entry(fenetre)
entree_auteur.pack()


label_statut=tk.Label(fenetre, text="Statut", fg="#F786FF", bg="#E6D3FF", pady=10)
label_statut.pack()

entree_statut=tk.Entry(fenetre)
entree_statut.pack()


label_genre=tk.Label(fenetre, text="Genre", fg="#F786FF", bg="#E6D3FF", pady=10)
label_genre.pack()

entree_genre=tk.Entry(fenetre)
entree_genre.pack()


label_note=tk.Label(fenetre, text="Note", fg="#F786FF", bg="#E6D3FF", pady=10)
label_note.pack()

entree_note=tk.Entry(fenetre)
entree_note.pack()


arbre=ttk.Treeview(
    fenetre,
    columns=("id","titre","auteur","statut","genre","note"),
    show="headings",
)

arbre.heading("id",text="ID")
arbre.heading("titre",text="Titre")
arbre.heading("auteur",text="Auteur")
arbre.heading("statut",text="Statut")
arbre.heading("genre",text="Genre")
arbre.heading("note",text="Note")

arbre.pack(fill="both", expand=True)

def ajouter():
    titre=entree_titre.get()
    auteur=entree_auteur.get()
    statut=entree_statut.get()
    genre=entree_genre.get()
    note=entree_note.get()

    ajouter_livre(
        titre,
        auteur,
        statut,
        genre,
        note
    )
    afficher()

    entree_titre.delete(0, tk.END)
    entree_auteur.delete(0, tk.END)
    entree_statut.delete(0, tk.END)
    entree_genre.delete(0, tk.END)
    entree_note.delete(0, tk.END)


def afficher():
    for fils in arbre.get_children():
        arbre.delete(fils)

    fils = afficher_livre()

    for livre in fils:
        arbre.insert(
            "",
            tk.END,
            values=livre
        )

bouton_ajouter=tk.Button(
    fenetre,
    text="Ajouter",
    command=ajouter
)
bouton_ajouter.pack()

######################################


def modifier():
    selection=arbre.selection()
    if selection:
        ligne=arbre.item(selection)
        id_livre=ligne["values"][0]
        
        titre=entree_titre.get()
        auteur=entree_auteur.get()
        statut=entree_statut.get()
        genre=entree_genre.get()
        note=entree_note.get()
        
        modifier_livre(
            id_livre,
            titre,
            auteur,
            statut,
            genre,
            note
            )
        afficher()

bouton_modifier=tk.Button(
    fenetre,
    text="Modifier",
    command=modifier
)
bouton_modifier.pack()


def supprimer():
    selection=arbre.selection()
    if selection:
        ligne=arbre.item(selection)
        id_livre=ligne["values"][0]
        supprimer_livre(id_livre)
        afficher()


bouton_supprimer=tk.Button(
    fenetre,
    text="Supprimer",
    command=supprimer
)
bouton_supprimer.pack()

def selectionner(event):
    selection=arbre.selection()
    if selection:
        ligne=arbre.item(selection)
        livre=ligne["values"]

        entree_titre.delete(0,tk.END)
        entree_titre.insert(0,livre[1])

        entree_auteur.delete(0,tk.END)
        entree_auteur.insert(0,livre[2])

        entree_statut.delete(0,tk.END)
        entree_statut.insert(0,livre[3])

        entree_genre.delete(0,tk.END)
        entree_genre.insert(0,livre[4])

        entree_note.delete(0,tk.END)
        entree_note.insert(0,livre[5])

arbre.bind("<<TreeviewSelect>>", selectionner)




afficher()

fenetre.mainloop()