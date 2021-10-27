def validar(email):
    caractervalido="@"
    emailValido = False
    for i in email:
        if i == caractervalido:
            return  True
    return False

E=input("Introduce tu Email: ")
if validar(E):
    print("Dirección valida")
else:
    print("Dirección invalida")