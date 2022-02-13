T = int(input())

for test in range(T):
    k = int(input())
    n = int(input())
    level = k + 1
    # 0층이 있는데 14층까지 있다 = 사실상 15층
    pep = [[0 for _ in range(14)] for _ in range(15)]
    # 0층은 가득차있다는 설정
    for a in range(1, 15):
        pep[0][a-1] = a
    # 0층 때문에 k + 1을 level로 그냥 표현
    for i in range(1, level):
        # n 호까지 채워넣기
        for j in range(n):
            # 1, 12, 123 을 반복해야 하므로 한번더
            for c in range(j+1):
                pep[i][j] += pep[i-1][c]

    print(pep[k][n - 1])


# 코드 간결하고 핵심만

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    # 0층 구현 (필요한 부분 까지만)
    people_list = [x for x in range(1, n + 1)] 
    # a층의 b호는 a-1층의 b호 + a층의 b-1 호이다.
    for floor in range(k):
        for row in range(1, n):
            people_list[row] += people_list[row - 1]

    print(people_list[-1])