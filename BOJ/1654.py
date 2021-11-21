import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []
for _ in range(a) :
  arr.append(int(input()))
result = 0
left = 0
right = max(arr)+1
cnt = 0
while left < right :
  mid = ( left + right ) //2
  sum = 0
  for i in arr :
    sum += i // mid
  if sum >= b :
    left = mid + 1
    result = mid
  elif sum < b :
    right = mid

print(result)