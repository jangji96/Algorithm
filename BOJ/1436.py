import sys
input = sys.stdin.readline

n = int(input())
count = 0
num = 0
while True :
  num += 1
  if '666' in str(num) :
    count += 1
    if count == n :
      print(num)
      break