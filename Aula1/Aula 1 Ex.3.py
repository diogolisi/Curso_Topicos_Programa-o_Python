print("digite um valor em segundos")
x = int(input())
hora = x//3600
min = (x%3600)//60
seg = (x%3600)%60

print(hora, "horas", min, "minutos", seg, "segundos")