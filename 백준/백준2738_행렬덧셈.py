# 백준 2738 행렬 덧셈
import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # 행렬의 크기는 n*m이다.

arr1,arr2=[],[]

for i in range(n):
    arr1.append(list(map(int,input().split())))

for j in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(arr1[i][j]+arr2[i][j],end=' ')
    print()
