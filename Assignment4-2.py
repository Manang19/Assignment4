a=[ ]
n = int(input("Enter the no. of Element: "))

for i in range  (n):
    x = int(input("enter the value:"))
    a.append ((x))
    print(a)

result = map(lambda a: a + a + a, a)
print(list(result))