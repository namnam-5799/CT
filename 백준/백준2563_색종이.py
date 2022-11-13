# 백준 2563 색종이

n = int(input())
arr = [[False]*100 for _ in range(100)]

for i in range(n):
    idx_x, idx_y = map(int,input().split())
    for j in range(idx_x,idx_x+10):
        for k in range(idx_y,idx_y+10):
            print(j,k)
            arr[j][k] = True

count = 0
for i in arr:
    count += i.count(True)
print(count)



