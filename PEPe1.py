counter=0
while counter<=3:

    string_seed=(input("Ingrese el numero aleatorio de N:"))
    size=len(string_seed)
    print("el numero tendra por ende cantidad de digitos:", size)
    string_number=int(string_seed)
    
    for i in range(4):
        if size < 5:
        
            number_1=(string_number)**2
            number_2=str(number_1)
            size2=len(number_2)
            first_size= int((size2-size)/2)
            number_4=(string_number)**2/10**8

            number_3=number_2[first_size: first_size + size]
            print( '{}. {}. {}'. format(string_number,number_1,number_4,number_3))
            string_number=int(number_3)

    if size>4:
        print("Lo siento, el numero ingresado es incorrecto, intentelo de nuevo:")
        counter=counter+1
    
    if counter ==3:
        print("Lo siento, ya has fallado 3 veces.")
        break