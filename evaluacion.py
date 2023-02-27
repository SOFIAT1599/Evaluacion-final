import json

#data={"Ferreteria":[]}

#with open ("test.json","w") as file:
    #json.dump(data,file,indent=2)

opcion=int(input("¿Que accion desea realizar?""\n"))

#1 Almacenar
#2 Leer
#3 Editar

if opcion==1:
    data={}
    with open ("test.json","r") as file:
        data = json.load(file)
        
    a=input("Ingresar el nombre del producto:")
    b=input("Ingresar descripcion:")
    c=input("Ingresar el precio:")

    data["Ferreteria"].append({
        "Nombre":a,"Descripcion":b,"Precio":c})
     
    print(data)
    
    with open ("test.json","w") as file:
        json.dump(data,file,indent=2)

    

if opcion==2:
        
    with open ("test.json","r") as file:
        data = json.load(file)  
        print(data) 

if opcion==3:
    data={}
        
    with open ("test.json","r") as file:
        data = json.load(file)
        
    d=input("Ingrese el valor a editar:")

for d in data["Ferreteria"]:
    if d in data["Ferreteria"]:
         
        with open ("test.json","w") as file:
            json.dump(data,file,indent=2)

    e=input("Ingrese el nuevo Nombre del producto:""\n")
    f=input("Ingrese la nueva Descripcion:""\n")
    g=input("Ingrese el nuevo Precio:""\n")

data["Ferreteria"][d].append({"Nombre":a,"Descripcion":b,"Precio":c})
print(data)

with open ("test.json","w+") as file:
    json.dump(data,file,indent=2)

