string_integer=input("Ingrese un numero entero:")
acumulador=0
k=0
n=string_integer


if n.isnumeric():
    number_1=int(n) 
    print("el valor", n , "es un entero")
    while k<number_1:
        k=k+1
        acumulador=acumulador + k
    print("Su suma es", acumulador)


else:
    print("error, intente de nuevo")
    print(" ")
    while not n.isnumeric:
        string_integer=input("Ingrese un numero entero:")
        number_1=int(n) 
    print("el valor", n , "es un entero")


            