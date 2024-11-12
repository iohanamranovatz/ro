"""
P3. Biblioteca

Scrieti o aplicatie pentru o bibliotecă. Aplicatia stochează:
• carti: <book_id>,<titlu>, <descriere>,<autor>,etc
• clienti: <client_id>, <nume>, <CNP>,etc
Creati o aplicatie care permite:
   1.gestiunea listei de carti si clienti:
          o adauaă, sterge, afisaza, lista de cărti, lista de clienti
"""


import sys,os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations.operatii_carte import adauga_carte, sortare_carti_dupa_titlu, sterge_carte, inchirieaza_carte, returneaza_carte, cauta_carte_dupa_autor
from operations.operatii_client import  cauta_client_dupa_nume, sterge_client, cauta_client,adauga_client,sorteaza_clienti_dupa_id

def ui_add_book(lista_carte):
    book_id = input("Introduceți ID-ul cărții: ")
    titlu = input("Introduceți titlul cărții: ")
    descriere = input("Introduceți descrierea cărții: ")
    autor = input("Introduceți autorul cărții: ")
    try:
       adauga_carte(lista_carte,book_id,titlu,descriere,autor)
    except ValueError:
            print("ID-ul introdus este deja in functiune!")

def ui_delete_book(lista_carte):
    afiseaza_carti(lista_carte)
    titlu=input("Introduce-ti TITLUl cartii care doriti sa o stergeti:")
    try:
        sterge_carte(lista_carte,titlu)
    except ValueError:
        print("Titlul introdus nu apartine listei de carti!")

def ui_inchireaza_carte(set_clienti,lista_inchirieri,lista_carte):
    afiseaza_carti(lista_carte)
    book_id=int(input("Introduce-ti ID-ul cartii care doriti sa o inchiriati:"))
    try:
        afiseaza_clienti_dupa_lista(set_clienti)
        client_id=int(input("Introduceți ID-ul clientului care închiriază cartea:"))
        inchirieaza_carte(book_id,client_id,lista_inchirieri) 
        print("Cartea a fost inchiriata cu succes!")
    except ValueError:
        print("Cartea este deja inchiriata!")


def ui_returneaza_carte(lista_carte,lista_inchirieri):
    if (len(lista_carte) == 0):
        print("Nu există cărți în listă.")
        return
    book_id = int(input("Introduceți ID-ul cărții de returnat: "))
    try:
        returneaza_carte(book_id,lista_inchirieri) 
        print("Cartea a fost returnata cu succes")
    except ValueError:
        print("Cartea nu este închiriată.")

def afiseaza_carti(lista_carte):
    """
    Afișează lista de cărți într-un format simplu.
    """
    print("\nLista de cărți:")
    if lista_carte:
        for carte in lista_carte:
            print(f"{carte[0]} - {carte[1]} de {carte[2]}") 


def afiseaza_clienti_dupa_lista(lista_client):
    """
    Afișează lista de clienți într-un format simplu.
    """
    print("\nLista de clienți:")
    if lista_client:
        for client in lista_client:
            print(f"{client[0]} - {client[1]} cu CNP-ul {client[2]}")


def afiseaza_clienti_set(set_clienti):
    """
    Afișează lista de clienți într-un format simplu.
    """
    print("\nLista de clienți:")
    if set_clienti:
        for client in set_clienti:
            print(f"{client[0]} - {client[1]} cu CNP-ul {client[2]}")


def ui_adauga_client(set):
    client_id = input("Introduceți ID-ul clientului: ")
    nume = input("Introduceți numele clientului: ")
    CNP = input("Introduceți CNP-ul clientului: ")
    try:
        adauga_client(set,client_id,nume,CNP) 
        print("Client adaugat!")
    except ValueError:
        print("ID-ul introdus este deja in functiune!")

def ui_sterge_client(set_client):
    if len(set_client)==0:
        print("Nu sunt clienti in lista!")
        return
    afiseaza_clienti_set(set_client)
    client_id = int(input("Introduceți ID-ul clientului de șters: "))
    try:
        sterge_client(set_client,client_id)
    except ValueError:
        print("Clientul introdus nu se afla in lista!")

def ui_cauta_carte_dupa_autor(lista_carte):
    if len(lista_carte)==0:
        print("Nu sunt carti in lista!")
        return
    print("Atentie! Cautarea este case-sensitive, va rugam sa introduceti numele corect!")
    autor=input("Introduce-ti autorul care doriti sa-l cautati:")
    try:
        carti_gasite=cauta_carte_dupa_autor(lista_carte,autor)
        print(carti_gasite)
    except ValueError:
        print("Nu a fost gasita nici o carte!")

def ui_cauta_client_dupa_nume(set_client):
    if len(set_client)==0:
        print("Nu sunt clienti in lista")
        return
    afiseaza_clienti_set(set_client)
    nume=input("Introduce-ti numele clientului pe care doriti sa-l cautati:")
    rez=cauta_client_dupa_nume(set_client,nume)
    if rez:
        print(rez)
        return
    print("Clientul nu a fost gasit!")


def ui_sortare_carti_dupa_titlu(lista_carti):
    if len(lista_carti)==0:
        print("Nu exista carti adaugate!")
        return
    lista_carti_sortata=sortare_carti_dupa_titlu(lista_carti)
    afiseaza_carti(lista_carti_sortata)
    

def ui_sorteaza_clienti_dupa_id(set_clienti):
    if len(set_clienti)==0:
        print("Nu ati adaugat clienti!")
    set_clienti=sorteaza_clienti_dupa_id(set_clienti)
    afiseaza_clienti_dupa_lista(set_clienti)
 

def afis():
    """
    Functie pentru afisarea Meniului.
    """
    print("Meniu:")
    print("1. Adaugă carte")
    print("2. Șterge carte")
    print("3. Adaugă client")
    print("4. Șterge client")
    print("5. Închirează carte")
    print("6. Returnează carte")
    print("7. Afișează lista de cărți")
    print("8. Afișează lista de clienți")
    print("9. Cauta client dupa nume")
    print("10. Cauta carte dupa autor")
    print("11. Sorteaza clienti dupa id")
    print("12. Sorteaza carti dupa titlu")
    print("x. Ieșire")


def run_menu(lista_carte, lista_inchirieri, set_clienti):
    print("Bine ați venit!")

 
    dict_carte = {1: ui_add_book, 2: ui_delete_book, 7: afiseaza_carti, 10: ui_cauta_carte_dupa_autor, 12: ui_sortare_carti_dupa_titlu}
    dict_client = {3: ui_adauga_client, 4: ui_sterge_client, 8: afiseaza_clienti_set,9:ui_cauta_client_dupa_nume,11: ui_sorteaza_clienti_dupa_id}
    dict_prestari_servicii = {5: ui_inchireaza_carte, 6: ui_returneaza_carte}

    while True:
        afis()
        optiune = input("Optiune: ")
        if optiune == "x":
            print("Ieșire din program.")
            break
        optiune=int(optiune)
        if optiune in dict_carte:
            dict_carte[optiune](lista_carte)
        elif optiune in dict_client:
            dict_client[optiune](set_clienti)
        elif optiune in dict_prestari_servicii:
            dict_prestari_servicii[optiune](lista_carte, set_clienti, lista_inchirieri)
        else:
            print("Opțiune invalidă. Alegeți o opțiune între 1 și 10 sau 'x' pentru ieșire.")