#ejercicio 1

word_1=input("Ingrese una palabra:")
word_2=input("ingrese otra palabra:")


if set(word_1)==set(word_2) and len(word_1)==len(word_2):
    print("Las palabras", word_1, "y", word_2, "son anagramas")

else:
    print("Las palabras", word_1, "y", word_2, "no son anagramas")
print(" ")

#ejercicio 2

list=0
string_1=input("Ingrese una frase: ")
string_list = string_1.split(" ")

for word in string_list:
    list+=1
    print("El primer caracter de la palabara", word, "es", word[0].title())

    if list==1: #primera iteracion
        character_1_word_1=word[0].title()
        character_1_next_word=word[0].title()
        print("caracter 1 de la palabra actual:",character_1_next_word, ";caracter 1 de la 1era. palabra:", character_1_word_1)
        print(" ")

    else: #para realizar la iteracion entre las demas palabras
        character_1_next_word=word[0].title()
        print("caracter 1 de la palabra actual:",character_1_next_word, ";caracter 1 de la 1era. palabra ", character_1_word_1)
        print(" ")
        if character_1_next_word!=character_1_word_1:
            print(string_1, "no es tautograma")
            print("end")
            quit()
print(" ")  
print("Respuesta")
print(string_1, "es tautograma")
print("end")