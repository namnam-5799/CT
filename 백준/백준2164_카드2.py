# 백준 2164 카드2
from collections import deque

n = int(input())

# 카드 만들기
cards =[]
for i in range(1,n+1):
    cards.append(i)
cards = deque(cards)

while len(cards)> 1:
    # 맨 앞의 카드를 버리고
    cards.popleft()
    # 맨 앞의 카드를 맨뒤에 붙인다
    cards.append(cards.popleft())
    print(cards)
print(cards[0])
