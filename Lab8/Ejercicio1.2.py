E=input("Introduce tu Email: ")
cadena=E.capitalize()
position= (cadena.find("@"))

if position !=-1:
    print("Correo valido")
else:
    print("Correo invalido")