import sys
from collections import deque

input = sys.stdin.readline
ans = -1

N = int(input())
startTime = []
endTime = []

for i in range(N):
  a, b, c = map(int, input().split())
  startTime.append([b, a])
  endTime.append([c, a])

startTime.sort(reverse = True)
endTime.sort(reverse = True)

temp = []

for i in range(endTime[0][0]+1):

  while startTime and i >= startTime[-1][0]:
    t, idx = startTime.pop()
    temp.append(idx)

  while endTime and i >= endTime[-1][0]:
    t, idx = endTime.pop()
    temp.remove(idx)

  if len(temp) > ans:
    result = len(temp)
print(result)