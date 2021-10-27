#Día

list=["Nothing","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day=int(input("Enter the number of the day: "))

if 1 <= day <= 7:
    print(f"The number {day} refers to {list[day]}")
else:
    print(f"The number {day} is unvaliable")