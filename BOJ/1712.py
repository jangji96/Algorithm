import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if(c-b <= 0) :
  i=-1
else :
  i = a//(c-b) +1

print(i)