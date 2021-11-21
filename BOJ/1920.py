import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

setA=set(A)

for i in B :
  if i in setA :
    print(1)
  else :
    print(0)