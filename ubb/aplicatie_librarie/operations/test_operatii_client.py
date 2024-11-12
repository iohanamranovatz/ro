import sys,os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations.operatii_client import creaza_client, sorteaza_clienti_dupa_id, sterge_client, cauta_client_dupa_nume

def cauta_client(set_client,id):
    """
    Funcție pentru căutarea unui client după id.
    """
    for client in set_client:
        if client[0] == id:
            return True
    return False
def test_adauga_client():
    set_client = set()  
    client = creaza_client(2, "Bianca", "1234567895")  
    set_client.add(client) 
    assert (len(set_client) == 1)

def test_sterge_client():
    set_client={(1,'Branco','54542454646')}
    sterge_client(set_client,set_client[0])
    assert (len(set_client)==0)

def test_cauta_client_dupa_nume():
    set_client={(9,'Adriana',"885545454")}
    clientul=cauta_client_dupa_nume(set_client,"Adriana")
    assert (clientul==(9,'Adriana',"885545454"))

def test_sorteaza_clienti_dupa_id():
    set_clienti={(90,"Mariana","5655656"),(45,"Adrian","6565686846"),(67,"MARIAN","565655"),(37,"Brigitte","2443546")}
    lista_clienti_sortata_manual=[(37,"Brigitte","2443546"),(45,"Adrian","6565686846"),(67,"MARIAN","565655"),(90,"Mariana","5655656")]
    lista_clienti_sortata_de_functie=sorteaza_clienti_dupa_id(set_clienti)
    assert (lista_clienti_sortata_de_functie==lista_clienti_sortata_manual)






