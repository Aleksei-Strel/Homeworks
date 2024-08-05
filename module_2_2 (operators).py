a = 15
b = 10
c = 15
if a==b==c:
    print(3)
if a==b!=c or a==c!=b or b==c!=a:
    print(2)
elif a != b != c:
    print(0)
