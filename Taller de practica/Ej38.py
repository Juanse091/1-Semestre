# Between 0 and 5

num = input("Enter 2 numbers (Separate with a ,): ")
num = (num.split(","))
n1= int(num[0])
n2 = int(num[1])

if 5 >= n1 >= 0 and 5 >= n2 >= 0:
    print("True")
else:
    print("False")