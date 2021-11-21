from collections import deque

N, K = map(int, input().split())
times = [0]*100001

q = deque()
q.append(N)
while q: 
  a = q.popleft()
  if a == K: 
    print(times[a])
    break;
  for i in (a-1, a+1, a*2):
    if 0 <= i < 100001 and not times[i]: 
      times[i] = times[a] + 1
      q.append(i) 