n = [3,5,2,4,1,3];
aux = 0
for i in range(0,len(n)):
    for j in range(0,len(n)):
        if n[i] < n[j]:
            aux=n[j]
            n[j] = n[i]
            n[i] = aux

for i in range(0,len(n)):
    print(n[i])