import sys
input = sys.stdin.readline

t = int(input())
arr = []

for _ in range(t) :
  arr.append(int(input()))
arr.sort()
for i in arr :
  print(i)