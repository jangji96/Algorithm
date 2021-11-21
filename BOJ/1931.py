import sys
input = sys.stdin.readline

arr = []

N = int(input())

for _ in range(N):
  n, m = map(int, input().split())
  arr.append([n,m])
arr.sort(key=lambda x: (x[1],x[0])) #뒤에거 기준 정렬 후 앞에거 정렬

end=0
result = 0

for i in range(N) :
  if arr[i][0] >= end:
    result += 1
    end = arr[i][1]

print(result)