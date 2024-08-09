# usuário digitará dez números.
# O programa deverá calcular quantos deles são maiores
# que dez.
controle = 0
for i in range(0,2):
    entrada = input('Digite um número ')
    numero = int(entrada)

    if numero > 10:
        controle+=1


print('Existem', controle, 'numero(s) maiores que 10')