def solution(participant, completion):
    d = dict()
    print(d)

    for person in participant:
        if person not in d:
            d[person] = 1
        else:
            d[person] += 1

    # 작은 반복문을 돌리는데,
    for c in completion:
        if c in d:  # 만약에 해당 값이 있다면 -1
            d[c] -= 1

    for key in d.keys():
        if d.get(key) == 1:
            return key  # 마지막 배열에 걸러진 사람만 출력
