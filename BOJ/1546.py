import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int,input().split()))
sumA = 0
maxA = max(arr)

for i in range(0,a) :
  sumA += arr[i]/maxA*100

print(sumA/a)