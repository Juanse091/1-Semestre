cont=0
def lenUltimaPalabra(cadena):
   if len(cadena)==0:
       return 0
   for i in range(len(cadena)):
       if cadena[i]!=' ':
           cont+=1
       else:
           if i<len(cadena)-1 and cadena[i+1]!=' ':
               cont=0
   return cont
cadena = input("Ingrese la cadena o frase = ")
if lenUltimaPalabra(cadena):
    print(lenUltimaPalabra(cadena))
