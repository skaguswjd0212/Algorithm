n = int(input())

i = 2

while (n != 1 and i<=n):
     while (n%i == 0):
        n = n//i
        print(i)
     i+=1