Hole_size=int(input("Ingrese el tamaño de profundidad del pozo:"))
amount_that_climbing=int(input("Ingrese la cantidad que tre3paba durante el dia:"))
quantify_that_descend=int(input("Ingrese la cantidad que desciende durante la noche:"))

condition_1= amount_that_climbing - quantify_that_descend

while condition_1 != Hole_size-1:
    if condition_1<=Hole_size-1:
        print("El caracol tardo aprox.", condition_1, "dias en salir del pozo")
    else:
        print("Error, el caracol no pudo salir del pozo")
        break
