
def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:  # 카테고리 이미 있으면 개수 추가
            dic[i[1]] += 1
        else:  # 카테고리 없으면 1로 초기화
            dic[i[1]] = 1

    values = dic.values()
    sum = 1

    for c in values:  # 조합수 구하는 식, 키의 값들을 돌면서
        sum *= (c + 1)  # 안입는 경우까지 고려해서 +1로 계산해서 곱해줌
    sum -= 1  # 문제에서 최소 한개는 입으니 모두 안입는 경우 빼야됨

    return sum