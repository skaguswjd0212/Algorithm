star = int(input())

for i in range(1, star):
    print((star-i)*' '+'*'*i)
print('*'*star)

for i in range(star-1, 0, -1):
    print((star-i)*' '+'*'*i)