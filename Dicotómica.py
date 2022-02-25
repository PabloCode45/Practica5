n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

num = int(input("Dame un número a buscar : "))

while(num<n[0] or num>n[len(n)-1]) :
    num = int(input("Número fuera de rango, dame otro número : "))

i = 0
j = len(n)
medio = j//2


while (n[medio]!=num) :
    medio=(i+j)//2
    if n[medio]>num :
        j=medio
    elif n[medio]<num:
        i=medio

print("El número está en la posición : "+str(medio))