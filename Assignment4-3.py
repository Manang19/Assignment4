a=[ ]
n = int(input("Enter the no. of Element: "))

for i in range  (n):
    x = int(input("enter the value:"))
    a.append ((x))
    print(a)


square_nolist = list(map(lambda x: x ** 2, a))
print(square_nolist)