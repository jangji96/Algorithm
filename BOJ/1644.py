import sys
input = sys.stdin.readline

N = int(input())

pCheck = [True for _ in range(N+1)]
primeArr = []

for i in range(2, int(N+1 ** 0.5)):
  if pCheck[i]:
    for j in range(i+i, N+1, i):
      pCheck[j] = False 

for i in range(2,len(pCheck)) :
  if pCheck[i] == True :
    primeArr.append(i)

result = 0
start = 0
end = 0

while end <= len(primeArr):
  temp_sum = sum(primeArr[start:end])
  if temp_sum == N:
    result += 1
    end += 1
  elif temp_sum < N:
    end += 1
  else:
    start += 1

print(result)