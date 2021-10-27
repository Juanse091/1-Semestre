while True:
    opcion = input("""Elige una fruta para tu desayuno:
    1- Manzanas
    2- Bananas
    3- Nada
    4- Otro
    Su respuesta es: """)#Creamos un input
        #que el usuario ingrese su opción y la almacenamos en "opcion"
    if opcion == "1": #Condionales según la opción que eligió!
        print("Has seleccionado manzanas")
        continue #Reiniciamos el bucle
    elif opcion == "2":
        print("Has seleccionado bananas")
        continue #Reiniciamos el bucle
    elif opcion == "3":
        print("Has seleccionado nada")
        continue #Reiniciamos el bucle
    elif opcion == "4": #Agregamos la opción con .lower para no tener problema con mayusculas
        r=input("Que otro alimento desea consumir: ")
        print(f"Has seleccionado {r}")
        continue #Reiniciamos el bucle
    else:
        print("Debemos selecionar una opcion (1, 2 o 3)")
    
    print("Programa terminado, que disfrutes tu desayuno") #Agregamos 
    #un print FUERA DEL BUCLE dar fin 

    