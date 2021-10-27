# Incrementa o disminuye

num = input("Enter 3 numbers (Separate with a , ): ")

num= num.split(",")

print (f"Numbers join{num}")

if num[0] < num[1] and num[1] < num [2]:
    print ("They are increasing")
elif num[0] > num[1] and num[1] > num[2]:
    print ("They are decreasing")
else:
    print ("They aren´t increasing or decreasing")