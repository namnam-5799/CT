def solution(lines):
    # 입력 받은 전체 선분을 배열에 담아서 가장 큰 값, 가장 작은값 뽑아내기
    list = sum(lines,[])
    #print(list) # [-1, 1, 1, 3, 3, 9]

    max_index = max(list)
    min_index = min(list)
    #print('최대, 최소 인덱스',max_index, min_index) 9,-1

    # 전체 좌표의 길이만큼 빈 배열을 생성
    # 음수일 수도 있으니 abs로 절댓값 씌
    arr = [0] * (abs(max_index)+abs(min_index)+1)
    # print('배열의 길이만큼 0배열 생성',arr)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # 반복문을 돌면서 구간에 도달할때까지 배열에 넣음
    for i in range(len(lines)):

        while lines[i][0]!=lines[i][1]:
            idx = lines[i][0] + abs(min_index) # 좌표랑 인덱스 맞추기 위해서
            arr[idx] += 1
            lines[i][0]+=1


    # 길이가 2 이상인 좌표는 겹치는 부분이므로 필터링해서 값으로 출력
    results = [x for x in arr if x>=2]
    return(len(results))


