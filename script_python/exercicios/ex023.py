num = int(input('Digite um número de 0 à 9999: '))
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print(''' Unidaded: {}
Dezena: {}
Centena: {}
Milhar: {}
'''.format(u, d, c, m))