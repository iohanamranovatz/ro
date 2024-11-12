import sys,os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations.operatii_carte import cauta_carte, sortare_carti_dupa_titlu, sterge_carte, inchirieaza_carte, returneaza_carte, verificare_inchiriere, cauta_carte_dupa_autor



def test_cauta_carte():
    lista_carte=["1",'vecinii','Mranovatz Brigitte',"descriere"]
    titlu=lista_carte[1]
    assert (cauta_carte(lista_carte,titlu))


def test_sterge_carte():
    lista_carte=[[2,"Galagie","Mihai Eminescu","descriere"],[1,'vecinii','Mranovatz Brigitte','descriere']]
    titlu=lista_carte[0][1]
    sterge_carte(lista_carte,titlu)
    assert (len(lista_carte)==1)

def test_inchirieaza_carte():
    book_id=25
    client_id=48
    lista_inchirieri=[]
    inchirieaza_carte(book_id,client_id,lista_inchirieri)
    assert (len(lista_inchirieri)==2)

def test_returneaza_carte():
    book_id=25
    lista_inchirieri=[25,48]
    returneaza_carte(book_id,lista_inchirieri)
    assert (len(lista_inchirieri)==0)

def test_verificare_inchiriere():
    lista_inchirieri=[25,48]
    book_id=25
    assert (verificare_inchiriere(lista_inchirieri,book_id)==True)

def test_cauta_carte_dupa_autor():
    lista_carte=[1,'vecinii','Mranovatz Brigitte','descriere']
    autor=lista_carte[2]
    assert (cauta_carte_dupa_autor(lista_carte,autor))



def test_sortare_carti_dupa_titlu():
    lista_carte=[(1,"Abecedar","Ion Creanga",'descriere'),(3,"X-Men","Marvel",'descriere'), (4 ,"Jurassic Park","Hollywood",'descriere')]
    lista_carte_sortata_manual=[(1,"Abecedar","Ion Creanga",'descriere'), (4 ,"Jurassic Park","Hollywood",'descriere'),(3,"X-Men","Marvel",'descriere')]
    lista_carte_sortata_functie=sortare_carti_dupa_titlu(lista_carte)
    assert (lista_carte_sortata_functie==lista_carte_sortata_manual)

def test_all():
    #test_adauga_carte()
    #test_cauta_carte()
    test_sterge_carte()
    test_inchirieaza_carte()
    test_returneaza_carte()
    test_verificare_inchiriere()
    test_cauta_carte_dupa_autor()
    test_sortare_carti_dupa_titlu()

test_all()
