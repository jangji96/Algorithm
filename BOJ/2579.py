import sys
input = sys.stdin.readline

t = int(input())

arr = [0]

for _ in range(t) :
  arr.append(int(input()))

dp = [0 for _ in range(t+1)]

for i in range(1,t+1) :
  dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])

print(dp[t])