import sys
input = sys.stdin.readline
import math

a = int(input())

def isPrime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True


li = list(range(2,10000))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

for _ in range(a) :
  n = int(input())
  for i in range(n//2,n) :
    if(i not in prime_li) :
      continue
    if(n-i in prime_li) :
      print(n-i,i)
      break