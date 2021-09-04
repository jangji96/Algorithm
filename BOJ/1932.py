import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n) :
  arr.append(list(map(int,input().split())))

dp = []
for i in range(1,n+1) :
  dp.append(list(0 for _ in range(i+1)))

for i in range(n) :
  for n in range(len(arr[i])) :
    dp[i][n] = arr[i][n] +  max(dp[i-1][n] , dp[i-1][n-1])

print(max(dp[n]))