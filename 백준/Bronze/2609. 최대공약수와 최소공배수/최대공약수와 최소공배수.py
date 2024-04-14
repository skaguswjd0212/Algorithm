a, b = input().split()
a, b = int(a), int(b)

if a > b:
    n = b
else:
    n = a

i = 2
grt = 1

while (n != 1 and i<=n):
     while (a%i == 0 and b%i == 0):
        grt *= i
        a = a//i
        b = b//i
     i+=1

low = grt*a*b
print(grt)
print(low)