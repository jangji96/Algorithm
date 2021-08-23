import sys
input = sys.stdin.readline

n = int(input())

for i in range(n) :
  if(n>i):
    for j in range(n-i-1) :
      print(' ',end='')
  for j in range(i+1) :
    print('*',end='')
  print()