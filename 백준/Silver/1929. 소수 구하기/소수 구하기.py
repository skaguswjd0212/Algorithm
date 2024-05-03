m, n = map(int, input().split())

for i in range(m, n+1):
    if i > 1:  # 1은 소수가 아니므로 제외
        #2부터 제곱근 사이 값 확인
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)

#참고: https://blognavercomcheetah254.tistory.com/46