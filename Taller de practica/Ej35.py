#Nombre en números
list =["Cero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

num=int(input("Please enter a number from 0 to 10: "))

if 0 <= num <= 10:
    print(f"The name of the number {num} is {list[num]}")
else:
    print("The number is unvaliable")