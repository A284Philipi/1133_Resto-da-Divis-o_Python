a = int(input())
b = int(input())
if (a > b):
    c = int(a)
    a = b
    b = c
a = a + 1
while (a < b):
    if (a%5 == 2 or a%5 == 3):
        print(a)
    a = a + 1