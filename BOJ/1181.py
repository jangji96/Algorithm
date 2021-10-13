import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  arr.append(input().strip())

arr=list(set(arr))
arr.sort()
arr.sort(key=len)

for i in arr :
    print(i)