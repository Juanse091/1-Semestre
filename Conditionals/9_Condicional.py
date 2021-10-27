N= int(input("Introducir número 1: "))
M= int(input("Introducir número 2: "))

I= float(N-1)

A= int(input("Introducir número 3: " ))

if A > M:
    M==A
    I==I-1
else:
    I==I-1
if I==0:
    print(M)
while I != 0:
    if A > M:
        M==A
    else:
        I=I-1
print(M)
