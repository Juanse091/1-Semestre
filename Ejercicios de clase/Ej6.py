print("Inicio del programa")
a=0 #Definimos una variable que nos ayudara en la suma de los productos
def IVA(price): #Definimos una función llamada IVA
    price= price * 19 / 100 #Calculamos el 19 porciento para el IVA

    return price #regresamos el valor del IVA (price) 

products= [] 
mony= input("Nombre de la moneda que se va a manejar: ") 
quanti=int(input("Cantidad de productos a cobrar: ")) 
for i in range(quanti): #Creamos un for in range para que el programa repita la cantidad de veces que fue solicitada

    name = input(f"Ingrese el nombre del producto {i+1}: ") 
    products.append(name) #Agregamos a la lista el nombre del producto
    value= float(input(f"Ingrese el valor de del producto {i+1}: ")) 
    print(f"Se ha ingresado el producto {name} con valor ${value} {mony.lower()}") 
    sum= a+value 
    a= sum

print(f"""Los productos ingresados son {products}
El IVA tiene una cantidad de: {IVA(a)}
En total se debe pagar: ${a+IVA(a)} {mony.lower()}""") #Imprimimos en pantalla los productos ingresados son
# También la cantidad del IVA, y el valor más el IVA
print("Fin del programa")