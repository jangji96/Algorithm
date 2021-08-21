import sys
input = sys.stdin.readline

n = int(input())
result =0

arr = []
for _ in range(n):
  arr.append(int(input()))

#역순 정렬
arr.sort(reverse=True)

index = -1

for i in arr :
  index = index + 1
  if(index%3==2) :
    continue
  result = result + i

print(result)