x, y = input().split()
x, y = int(x), int(y)

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = 0

for i in range(1, x):
    day += month[i]
   
day_of_week = (day+y)%7
    
print(week[day_of_week])