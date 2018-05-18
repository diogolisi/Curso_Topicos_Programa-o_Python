'''x = int (input())
n = 0
while n<=10:
    print (x*n)
    n+=1
'''
'''
print('Meu nome é: ')
for i in range(5):
    print('Jimmy')
'''
'''
for i in range(12, 16):
    print(i)
'''
'''
for i in range (0, 10, 2):
    print(i)
'''

import sys

while True:
    print('Digite exit para sair do programa.')
    resposta = input()
    if resposta == 'exit':
        sys.exit()
    print(f'Você digitou {resposta}')