from collections import deque

n, m = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int, input())))

q = deque()
q.append((0,0,1))
disArr=[[n*m] * m for _ in range(n)]

while q :
  x, y, dis= q.popleft()

	#목적지 도착하면 출력 후 종료
  if (n-1)==x and (m-1)==y :
    print(dis)
    break

	# 미로크기 넘어가거나 벽에 막히면 패스
  if x<0 or y<0 or x>=n or y>=m or arr[x][y]==0:
    continue
   
  #새로 찾은 거리가 기존 저장한 거리보다 더 작고, 방문한적 없으면 다음 갈장소 탐색
  if dis < disArr[x][y] and disArr[x][y]==n*m :
    disArr[x][y] = dis
    
    q.append((x+1,y,dis+1))
    q.append((x-1,y,dis+1))
    q.append((x,y+1,dis+1))
    q.append((x,y-1,dis+1))