print('Dame el límite : ', end = '')
limite = int(input('Dame el límite : '))
cadena = ''
for x in range(limite):
    if(x%2==0):
        cadena+=str(x)+', '

print(cadena)