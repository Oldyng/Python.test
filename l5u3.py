# A - Mike Cash, B - Ivan Cash, X - Sum Inv
a = int(input())
b = int(input())
x = int(input())

if (a >= x) and (b >=x):
    print("2")
elif (a >=x):
    print("Mike")
elif (b >=x):
    print("Ivan")
elif (a + b >= x):
    print("1")
else:
    print("0")


