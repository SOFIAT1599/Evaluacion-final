n=int(input("Por favor ingresa un numero par:"))

while n<0 or n%2==1:
    n=int(input("Por favor ingresa un numero par:"))

#Generar matriz
matrix=[]
row1=[]
counter=1

for j in range(0,n):
    fila=[]
    if j==0:
        for i in range(1,n+1):
            row1.append(i)
        matrix.append(row1)

    elif j<(n/2):
        for i in range(0,n):
            fila.append(row1[int(i)]+2*n*j)
        matrix.append(fila)

    else:
        for i in range(0,n):
            fila.append(row1[int(i)]+n*(n-counter))
        matrix.append(fila)
        counter+=2
for m in matrix:
    print(m)

for j in range(0,n):
    print(j)
    
    

        
        






    
    
                
            
    