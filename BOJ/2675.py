import sys
input = sys.stdin.readline

a = int(input())
arr = []

for _ in range(a) :
  arr=list(input().split())
  for i in arr[1] :
    for _ in range(int(arr[0])) :
      print(i, end='')
  print()
