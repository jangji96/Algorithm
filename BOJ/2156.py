import sys
from collections import deque
input = sys.stdin.readline

a = int(input())

arr = []
for _ in range(a) :
  arr.append(int(input()))

result = 0

q = deque()
q.append((0,0,0,0)) #  총 마신 양 / 연속 마신 수 / 마실지 말지 선택한 잔 수

while q : 
  allMl, combo, passCnt, allCnt = q.popleft() 
  
  if allCnt+1 >= len(arr) :
    if result < allMl :
      result = allMl
    continue

  if combo +1 != 3 :
    q.append((allMl+arr[allCnt],combo+1,0,allCnt+1))
  if(passCnt +1 != 2) :
    q.append((allMl,0,passCnt+1,allCnt+1))
  
print(result)
