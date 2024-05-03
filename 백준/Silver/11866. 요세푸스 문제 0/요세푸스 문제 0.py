from collections import deque

n, k = map(int, input().split())

removed_list = []
queue = deque()

#큐에 1~N 삽입
for i in range(1, n+1):
    queue.append(i)

#큐가 빌 때까지
while queue:
    #k번째 값을 찾기 위해
    #큐에서 k-1개의 값을 pop하고 맨 뒤에 append
    for i in range(k-1):
        queue.append(queue.popleft())
    #결과 리스트에 k번째 값을 넣음
    removed_list.append(queue.popleft())

print("<", end='')
for i in range(len(removed_list)):
    print(removed_list[i], end='')
    if i == len(removed_list)-1:
        break
    print(", ", end='')
print(">")
