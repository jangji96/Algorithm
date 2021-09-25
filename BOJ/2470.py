import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int, input().split()))
items.sort()

start = 0
end = len(items)-1

a = items[start]
b = items[end]

sumN = sys.maxsize

while start < end :

  if abs(sumN) > abs(items[start]+items[end]) :
    a = items[start]
    b = items[end]
    sumN = a+b

  if items[start]+items[end] == 0 :
    break
  elif items[start]+items[end] < 0 :
    start += 1
  else :
    end -= 1

print(a,b)