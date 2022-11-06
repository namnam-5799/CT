# 프로그래머스 평행

# 직선의 기울기 : y2-y1/ x2-x1

# 비교 가능한 경우 :3
# 0번째,1번째 - 2,3
# 0,2 =  1,3
# 0,3 =  1,2

dots = [[0,0],[1,1],[2,2],[3,5]]
dots = sorted(dots)

# 0번째와 1번째 , 2번째와 3번째 좌표를 비교
incline0_1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
incline2_3 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])

if incline2_3 == incline0_1:
    print(1)

    # 0번째와 2번째, 1번째와 3번째 좌표를 비교
incline0_2 = (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0])
incline1_3 = (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0])

if incline1_3 == incline0_2:
    print(1)

    # 0번째와 3번째, 1번째와 2번째 좌표를 비교
incline0_3 = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
incline1_2 = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])

if incline1_2 == incline0_3:
    print(1)

print(0)
