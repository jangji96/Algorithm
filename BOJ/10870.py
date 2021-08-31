import sys
input = sys.stdin.readline

a=int(input())

def fibo(a) :
  if a==0 :
    return 0
  elif a==1 :
    return 1
  else :
    return fibo(a-1)+fibo(a-2)

result=fibo(a)
print(result)