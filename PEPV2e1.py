#Problema 1 (Doc2)
#Diseñe un programa que permita conocer cual es el porcentaje de numeros enteros menor a un valor N (leido como dato) cuya cadena llega al numero 89.

def suma_digitos_al_cuadrado(numero):
    suma_digitos=0
    for num in range(len(str(numero))):

        suma_digitos+=int(str(numero)[num])**2
    return suma_digitos

N=int(input("Ingrese un numero entero positivo:"))

contador_menor_N=0


for i in range(N):
    Aux_N=i+1

    while (Aux_N!=1 and Aux_N!=89):
        
        Aux_N=int(suma_digitos_al_cuadrado(Aux_N))

        if Aux_N==89:
            contador_menor_N+=1
            

print("Desde 1 hasta", N, "hay", contador_menor_N, "numeros que llegan a 89")
print("Obteniendose que el porcentaje de numeros que llegan a 89 es el de", round(contador_menor_N*100/N,2),"%")

 
