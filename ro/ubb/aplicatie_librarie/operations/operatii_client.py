import sys,os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from domain.entitatea_client import creaza_client
def cauta_client(set_client,id):
    """
    Funcție pentru căutarea unui client după id.
    """
    for client in set_client:
        if client[0] == id:
            return True
    return False

def adauga_client(set_client:set,client_id,nume,CNP):
    """
    Funcție pentru adăugarea unui client.
    """
    
    if cauta_client(set_client,id)==True:
        raise ValueError
    client_nou = creaza_client(client_id, nume, CNP)
    set_client.add(client_nou)

def sterge_client(set_client,client_id):
    """
    Funcție pentru ștergerea unui client după ID.
    """
    if cauta_client(set_client, id) == False:
        raise ValueError
    for client in set_client:
        if client[0]==client_id:
                client_to_remove=client
    set_client.remove(client_to_remove)

def cauta_client_dupa_nume(set_client,nume):
    for client in set_client:
        if client[1]==nume:
            return client
    return None

def extrage_id(x):
    return x[0]

def sorteaza_clienti_dupa_id(set_clienti):
    #fiindca set-ul nu are o ordine anume si nu poate fi sortat, il vom converti intr-o lista
    lista_clienti_sortata_dupa_id=sorted(set_clienti, key=extrage_id)
    return lista_clienti_sortata_dupa_id


