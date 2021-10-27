#Calculate a Discount

compra= int(input("Favor digite el valor de la compra:"))
compra_20= float(compra*20/100)
descuento= float(compra - compra_20)

#Se ultiliza int en el print, para que el resultado nos lo de en entero
if compra > 1000:
    print("El total a pagar sera de:", int(descuento), "$" )

else:
    print("El total a pagar sera de:", compra, "$")