import sys
input = sys.stdin.readline

a=int(input())

for i in range(9) :
  print(a, '*', (i+1), '=', (a*(i+1)))