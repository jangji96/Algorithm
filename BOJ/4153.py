import sys
input = sys.stdin.readline

while True :
  arr = list(map(int,input().split()))
  maxN = max(arr)
  if maxN == 0 :
    break
  arr.remove(maxN)
  if arr[0]**2 + arr[1]**2 == maxN ** 2 :
    print('right')
  else :
    print('wrong')