#Digitos de 1 numero

digit= (input("Enter a number: "))

digi= digit.split(".")
digi= int("".join(digi))

if digi < 100000:
    print(f"The number {digit} has {len(str(digi))} digits")
else:
    print(f"The number {digit} is unvalaible")