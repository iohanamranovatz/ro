
def creaza_client(client_id, nume, CNP):
    """
    Funcție pentru crearea unui nou client, reprezentat ca un tuplu.
    """
    return (client_id, nume, CNP)

"""
Getter accesează atributele clientului folosind indecșii specifici fiecărui
atribut (0 pentru client_id, 1 pentru nume, 2 pentru CNP).
"""
def get_client_id(client):
    return client[0]

def get_client_nume(client):
    return client[1]

def get_CNP(client):
    return client[2]

