t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    bg = [[0 for _ in range(M+1)] for _ in range(M+1)]
    for i in range(M + 1):
        for j in range(M + 1):
            if i == 1:
                bg[i][j] = j
            elif i == j:
                bg[i][j] = 1
            else:
                bg[i][j] = bg[i-1][j-1] + bg[i][j-1]
    print(bg[N][M])