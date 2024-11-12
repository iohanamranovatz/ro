def creaza_carte(book_id, titlu, descriere, autor):
    """
    Funcție pentru crearea unei noi cărți, reprezentată sub formă de listă.
    """
    return [book_id, titlu, descriere, autor]


"""
Getter si setter accesează sau modifică elementele din listă folosind indexii 
 specifici fiecărui atribut (0 pentru book_id, 1 pentru titlu, 2 pentru descriere, 3 pentru autor).
"""
def get_id(carte):
    return carte[0]

def set_id(carte, book_id):
    carte[0] = book_id

def get_titlu(carte):
    return carte[1]

def set_titlu(carte, titlu):
    carte[1] = titlu

def get_descriere(carte):
    return carte[2]

def set_descriere(carte, descriere):
    carte[2] = descriere

def get_autor(carte):
    return carte[3]

def set_autor(carte, autor):
    carte[3] = autor

