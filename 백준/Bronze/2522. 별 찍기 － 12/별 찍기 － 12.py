star = int(input())

for i in range(1, star+1):
    print((star-i)*' '+'*'*i)

for j in range(1, star):
    print(' '*(j)+(star-j)*'*')