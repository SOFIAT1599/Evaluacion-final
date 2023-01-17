#Problema 3 (Doc1)
#Realice un programa que genere una lista de listas, que emule a una matriz de orden NxM, con N y M dados por el usuario. Suponga que dicha matriz esta llena de la forma zig-zag horizontal. 

n=int(input("ingresa el numero de filas:"))
m=int(input("Ingresa el numero de columnas:"))

#generar matriz
matrix=[]
for j in range(0,n):
    fila=[]
    for i in range(0,m):
        fila.append(1 +(m*j) +i) 
    if j%2==1:
        fila.reverse()

    matrix.append(fila)   
for x in matrix:  
    print(x)
