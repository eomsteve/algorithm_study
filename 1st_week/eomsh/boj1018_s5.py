def chess(chess_map, w_map, b_map):
    w_cnt, b_cnt = 0, 0
    for x in range(8):
        for y in range(8):
            if chess_map[x][y] != w_map[x][y]:
                w_cnt += 1
            if chess_map[x][y] != b_map[x][y]:
                b_cnt += 1
    return w_cnt if w_cnt < b_cnt else b_cnt

# 입력
M, N = map(int, input().split())
# 입력
arr_map = [input() for _ in range(M)]

min_val = 65
w_ans = []
b_ans = []

# 정답 배열 생성 : w가 첫번째일떄, b가 첫번째일때
for i in range(8):
    if i % 2 == 0:
        b_ans.append('BWBWBWBW')
        w_ans.append('WBWBWBWB')
    else:
        b_ans.append('WBWBWBWB')
        w_ans.append('BWBWBWBW')

# 비교할 배열 생성
for i in range(M - 7):
    for j in range(N - 7):
        my_map = []
        for a in range(i, i + 8):
            rows = ''
            for b in range(j, j + 8):
                rows += arr_map[a][b]
            my_map.append(rows)
            # 함수를통해 배열 비교
        result = chess(my_map, w_ans, b_ans)
        if result < min_val:
            min_val = result

print(min_val)