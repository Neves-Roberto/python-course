#chance e probabilidade da mega sena
from math import factorial
total_cartela = 60
aposta = int(input('Digite quantos numeros apostados: '))
combinacao = (factorial(total_cartela))/((factorial(aposta))*factorial(total_cartela - aposta))
print('Chance de ganhar {:.10f} % '.format(1/combinacao*100))
