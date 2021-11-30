import sys
input = sys.stdin.readline

dp = [0 for _ in range(12)]

dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,12) :
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

T = int(input())

for _ in range(T) :
  num = int(input())
  print(dp[num])