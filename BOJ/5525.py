import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
S = S + 'xx'
result = 0
cnt=0

for i in range(1,M) :
  if i == M:
    break

  if S[i] == 'O' and S[i-1] =='I' and S[i+1] =='I' :
    cnt += 1
    if S[i+2] == 'O' and S[i+3] == 'I':
      continue
    else:
      if cnt >= N :
        result += cnt - N + 1
      cnt = 0

print(result)