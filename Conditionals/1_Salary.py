#Calculate the salary of a people.

horasT=float(input("Digite las horas trabajadas:"))
horasExt=float(horasT-40)

pago=int(horasT*20000)
pagoExt=int(horasExt*30000)


if horasT <= 40:
    print("Su salario es:", pago)

else:
    print("Su salario extra será:", "$", pagoExt + 80000,)