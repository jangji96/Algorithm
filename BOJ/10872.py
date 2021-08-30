import sys
input = sys.stdin.readline

a = int(input())

def fac(a) :
  if a > 1 :
    return a*fac(a-1)
  else :
    return 1

result = fac(a)
print(result)