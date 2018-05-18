print ('digite a frequência do aluno em %, apenas o número')
a = float (input())
if a<75:
    print('O aluno está reprovado')
else:
    print ('digite a média final do aluno')
b = float (input())
if a >= 75 and b >= 7:
    print('O aluno foi aprovado')
elif a >= 75 and (b <= 7 and b>=3):
    print('o aluno foi para prova final')
    c = float(input('Digite a nota da pf: \n'))
    if (b+c)/2 >=5:
        print('O aluno foi aprovado')
elif a >= 75 and b<3:
    print('o aluno foi reprovado')
elif a<75 or (b+c)/2<5:
    print ('o aluno está reprovado')
