import sys
input = sys.stdin.readline
from math import gcd

T = int(input())

for _ in range(T) :
  M, N, X, Y = map(int,input().split())
  lcm = (N * M)//gcd(N,M)
  year = Y
  target = 0
  
  # for _ in range(M) :
  #   if year > lcm :
  #     print(-1)
  #     break;

  #   if year % M != 0 :
  #     target = year % M
  #   else :
  #     target = M

  #   if target == X:
  #     print(year)
  #     break
  #   year += N

  for _ in range(N) :
    if X > lcm :
      print(-1)
      break;
    if (X - Y) % N == 0:
      print(X)
      break;
    X += M

