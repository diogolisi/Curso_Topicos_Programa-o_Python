print ('digite um número ')
a = int (input())
print ('digite outro número ')
b = int (input())
print ('Qual operação que você deseja fazer? \nPara soma digite "+" e para multiplicação digite "*"')
c = str (input())
if c == "+":
    print (a+b)
elif c == "*":
    print (a*b)