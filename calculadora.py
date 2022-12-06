mensaje_inicio="Bienvenido.Tienes 4 intentos"
print(mensaje_inicio)

contador=0
while contador<=4:
    
    num_1 = int(input ("Introduzca el primer numero:" ) )
    num_2 = int(input ("Introduzca el segundo numero:" ) )

    eleccion=int(input("Indique la operacion a realizar:"))
    eleccion<=4           
    #1)suma
    #2)resta
    #3)multiplicacion
    #4)division
  
    if eleccion == 1:
        print(" ")
        print(num_1+num_2) 
        print=(" ")
        

    if eleccion ==2:
        print(" ")
        print(num_1-num_2)
        print(" ")
        

    if eleccion ==3:
        print(" ")
        print(num_1*num_2)
        print(" ")
        

    if eleccion ==4:
        if num_2==0:
            print("indefinido")
            
        else:
            print(" ")
            print(float(num_1/num_2))
            print(" ")  
            
    if eleccion>4:
        print(" ")
        print("Operacion incorrecta, intente de nuevo")
        print(" ")
        contador=contador+1

    if contador==4:
        print(" ")
        print("Has fallado los 4 intentos")
        print(" ")
        break
    
