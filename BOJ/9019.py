import sys
input = sys.stdin.readline
from collections import deque

T=int(input())

for _ in range(T) :
  sNum, eNum = map(int, input().split())

  q = deque([[sNum,""]])
  visit = [0 for _ in range(10000)]
  visit[sNum] = 1

  while q :
    num, change = q.popleft()

    if num == eNum :
      print(change)
      break;
    
    if visit[num * 2 % 10000] != 1:
      visit[num * 2 % 10000] = 1
      q.append([num * 2 % 10000, change + "D"])

    if num == 0 :
      visit[9999]
      q.append([9999, change+"S"])
    else :
      visit[num - 1] = 1
      q.append([num - 1, change + "S"])

    if visit[num % 1000 * 10 + num // 1000] != 1:
      visit[num % 1000 * 10 + num // 1000] = 1
      q.append([num % 1000 * 10 + num // 1000, change + "L"])

    if visit[num % 10 * 1000 + num // 10] != 1:
      visit[num % 10 * 1000 + num // 10] = 1
      q.append([num % 10 * 1000 + num // 10, change + "R"])