#Problema 2 (Doc2)
#Realice un programa que calcule el valor de pi mediante el desarrollo de la serie.

string_number=int(input("ingrese la cantidad de terminos:"))
suma=0
for i in range(1,string_number):
    if i%2!=0:
        suma=suma+(1/(i)**6)
    else:
        suma=suma-(1/(i)**6)
    print("Pi:" +str(suma))  