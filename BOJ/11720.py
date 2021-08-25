import sys
input = sys.stdin.readline

a = int(input())
arr=list(input().strip())
sum = 0

for i in arr :
  sum += int(i)
print(sum)