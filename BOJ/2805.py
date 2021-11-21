import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
  mid = (start+end) // 2
  
  sumTree = 0

  for i in trees:
    if i >= mid:
      sumTree += i - mid
  
  if sumTree >= m:
    start = mid + 1
  else:
    end = mid - 1
    
print(end)