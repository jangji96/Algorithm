import sys
input = sys.stdin.readline

N,M = map(int,input().split())
cnt = 0
cMatrix=[]
rMatrix=[]
for i in range(N):
  cMatrix.append(list(map(int, input().strip())))

for i in range(N) :
  rMatrix.append(list(map(int, input().strip())))

def change(i,j):
  for a in range(i,i+3):
    for b in range(j,j+3):
      cMatrix[a][b] = 1 - cMatrix[a][b]

for i in range(0,N-2):
  for j in range(0,M-2):
    if cMatrix[i][j] != rMatrix[i][j]: 
      change(i,j)
      cnt += 1

impossible = False

for i in range(0,N):
  for j in range(0,M):
    if cMatrix[i][j] != rMatrix[i][j]:
      impossible = True
      break;

if(impossible):
  print(-1)
else:
  print(cnt)