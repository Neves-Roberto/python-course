def lista_grande(n):
    import random
    lista = []
    for i in range(n):
        lista.append(random.randrange(n))
    return lista