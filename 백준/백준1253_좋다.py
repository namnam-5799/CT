# 백준 1253 좋다
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int,input().split())))

now = 1 # nowf로 1부터 하나씩 증가시킬 예정
num1 = 0 # 앞에서부터
num2 = 0 # 뒤에서부터
count = 0

while now != n+1:
    print('-----현재 now의 값은----',now)
    sum = nums[num1] + nums[num2]
    print('현재 sum의 값',sum , '앞',nums[num1],'뒤',nums[num2])

    # 처음 인덱스나 마지막 인덱스가 now와 같아지면 수가 없다고 판단, 다음now로 넘긴다.
    if (now == nums[num1] or now == nums[num2]) and (nums[num1]!=0 and nums[num2]!=0) :
        print('수가 중복입니다. 다음 now를 검색합니다. ')
        now+=1
        continue

    if now == sum and nums[num1]!= nums[num2]: # 좋은수이면
        print('좋은 수 이므로 다음수를 검사 now증가')
        count += 1 # 카운트 증가
        now += 1 # 다음 수를 검사

    elif sum > now: # 합친 값이 now보다 크다면
        print('앞 인덱스로 이동')
        num1 +=1 # 한칸 이전의 수를 검색

    else: # 합친 값이 now보다 작다면
        print('뒤 인덱스로 이동')
        num2 += 1 # 한칸 이후의 수를 검색


print(count)