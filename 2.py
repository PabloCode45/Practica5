lista = list(input('Dame una palabra : '))
c=0

for x in range(len(lista)):
    if(lista[x] == 'a' or lista [x]=='e' or lista [x]=='i' or lista [x]=='o' or lista [x]=='u'):
        c+=1

print('Hay',c,'vocales.')