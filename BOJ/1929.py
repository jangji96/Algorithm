import sys
input = sys.stdin.readline
import math

a, b =map(int, input().split())

for num in range(a, b+1):
  error = 0
  if num > 1 :
    for i in range(2, int(math.sqrt(num))+1):
      if num % i == 0:
        error += 1
        break 
    if error == 0:
      print(num)