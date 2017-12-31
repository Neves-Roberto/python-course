class Carro:
    pass
# Classe iniciada vazia com o pass


#criando uma instancia
meu_carro = Carro()
print(meu_carro)
carro_do_ime = Carro()
print(carro_do_ime)

meu_carro.ano = 2004
meu_carro.modelo = 'celta'
meu_carro.cor = 'preto'
carro_do_ime.ano = 2010
carro_do_ime.modelo = 'Tesla'
print(meu_carro.ano)
print(meu_carro.cor)
print(meu_carro.modelo)
print(carro_do_ime.modelo)
print(type(meu_carro))
