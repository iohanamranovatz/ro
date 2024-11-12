import sys,os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from domain.entitatea_carte import creaza_carte

def cauta_carte(lista_carte: list, titlu: str):
    """
    Funcție pentru căutarea unei cărți după titlu.
    Args:
        lista_carte: lista de cărți unde fiecare carte este [book_id, titlu, descriere, autor]
        titlu: titlul cărții căutate
    Returns:
        lista cu cărțile găsite sau None dacă nu există
    """
    if not lista_carte:
        return None
        
    rezultate = []
    for carte in lista_carte:
        if isinstance(carte, list) and len(carte) >= 4:
            if str(carte[1]).lower() == str(titlu).lower():
                rezultate.append(carte)
    return rezultate if rezultate else None

def adauga_carte(lista_carte,book_id:str,titlu:str,descriere:str,autor:str):
    if cauta_carte(lista_carte,titlu):
        raise ValueError
    carte_noua = creaza_carte(book_id, titlu, descriere, autor) 
    lista_carte.append(carte_noua)


def inchirieaza_carte(book_id,client_id,  lista_inchirieri: list,):
    """
    Funcție pentru închirierea unei cărți.
    """
    if verificare_inchiriere(lista_inchirieri, book_id) == True:
        raise ValueError

    inchiriere = {"book_id": book_id, "client_id": client_id}
    lista_inchirieri.append(inchiriere)



def returneaza_carte(book_id, lista_inchirieri: list):
    """
    Funcție pentru returnarea unei cărți.
    """

    if verificare_inchiriere(lista_inchirieri, book_id) == False:
        raise ValueError

    for inchiriere in lista_inchirieri:
        if inchiriere['book_id'] == book_id:
            lista_inchirieri.remove(inchiriere)


def verificare_inchiriere(lista_inchirieri: list, book_id: int):
    """
    Verifică dacă o carte este deja închiriată.

    :param lista_inchirieri: Lista de închirieri.
    :param book_id: ID-ul cărții de verificat.
    :return bool: True dacă cartea este deja închiriată, False altfel.
    """
    for inchiriere in lista_inchirieri:
        if inchiriere['book_id'] == book_id:
            return True
    return False


def cauta_carte_dupa_autor(lista_carte, autor):
    """
    Funcție pentru căutarea cărților după autor
    Args:
        lista_carte: lista de cărți unde fiecare carte este [book_id, titlu, descriere, autor]
        autor: numele autorului căutat
    Returns:
        lista cu cărțile găsite
    """
    carti_gasite = []
    for carte in lista_carte:
        if isinstance(carte, list) and len(carte) >= 4:
            if str(carte[3]) == str(autor):
                carti_gasite.append(carte)
    if len(carti_gasite) == 0:
        raise ValueError
    return carti_gasite

def sterge_carte(lista_carte: list, titlu: str):
    """
    Funcție pentru ștergerea unei cărți după titlu.
    Ridică ValueError dacă cartea nu există.
    """
    carti_gasite = cauta_carte(lista_carte, titlu)
    if not carti_gasite:
        raise ValueError("Cartea nu există în listă")
    
    for carte in carti_gasite:
        lista_carte.remove(carte)
    return lista_carte

def extrage_titlu(x):
    return x[1]

def sortare_carti_dupa_titlu(lista_carti):
    lista_carti_sortata_dupa_titlu=sorted(lista_carti , key=extrage_titlu)
    return lista_carti_sortata_dupa_titlu

