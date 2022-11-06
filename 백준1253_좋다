# 백준 1253 좋다
import sys
input = sys.stdin.readline

N = int(input())
Result = 0
A = sorted(list(map(int, input().split())))

for k in range(N): # For문을 통해 배열을 순회하며 배열 전체를 검사.
    find = A[k] # 찾아야 할 값은 배열의 k번째 값
    num1 = int(0) # 시작 인덱스는 0
    num2 = int(N - 1) # 종료 인덱스는 전체 길이 -1

    while num1 < num2: # 두개의 포인터가 같아지는 시점에서 종료
        if A[num1] + A[num2] == find:  # find는 서로 다른 두 수의 합 이어야 함을 체크
            if num1 != k and num2 != k: # 같은 조건에서 앞, 뒤 포인터값과 합 자체가 같으면 안됨,
                Result += 1
                break

            # 둘 중 하나의 값과 겹치는 경우에는 (예: 구할 값이 3인데 현재 1,3인 경우 앞으로 당겨야한다.)
            # 다른 가능한 조합을 찾아야하므로 포인터를 조절
            elif num1 == k:
                num1 += 1
            elif num2 == k:
                num2 -= 1

        # 합한 결과보다 구해야 할 값이 작은 경우
        # 앞 포인터를 이동시켜 값을 키운다.
        elif A[num1] + A[num2] < find:
            num1 += 1
        else:
            num2 -= 1
print(Result)
