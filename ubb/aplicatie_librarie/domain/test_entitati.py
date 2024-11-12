import sys,os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from domain.entitatea_carte import creaza_carte
from domain.entitatea_client import creaza_client

def test_creaza_carte():
    assert creaza_carte('1','Capitan la cincisprezece ani','carte despre marinari','Jules Verne')=={'book_id': '1', 'titlu': 'capitan la cincisprezece ani','descriere': 'carte despre marinari', 'autor':'Jules Verne' }


def test_creaza_client():
    assert creaza_client('1','Denisa','1234567890')=={'client_id': '1', 'nume': 'Denisa','CNP': '1234567890'}


def test_all():
    test_creaza_carte()
    test_creaza_client()