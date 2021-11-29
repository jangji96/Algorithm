import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

arr = [i for i in range(n+1)]

def find(a) :
  if arr[a]==a :
    return arr[a]
  arr[a]=find(arr[a])
  return arr[a]

def union(a,b) :
  a=find(a)
  b=find(b)
  if a < b :
    arr[b] = a;
  else :
    arr[a] = b;

for _ in range(m) :
  x, a, b = map(int, input().split())

  if x :
    if find(a) == find(b) :
      print('YES')
    else :
      print('NO')
  else :
    union(a,b);
    