import sys
input = sys.stdin.readline
from math import gcd

T = int(input())

for _ in range(T) :
  M, N, X, Y = map(int,input().split())
  lcm = (N * M)//gcd(N,M)
  num = Y
  target=1
  
  for _ in range(M) :
    if num > lcm :
      print(-1)
      break;
    if num % M != 0 :
      target = num % M
    else :
      target = M
    if target == X:
      print(num)
      break
    num += N