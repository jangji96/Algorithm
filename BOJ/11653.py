import sys
input = sys.stdin.readline

a=int(input())
num = 2
while a != 1 :
  if a % num == 0 :
    a = a // num
    print(num)
  else :
    num = num + 1