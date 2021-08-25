import sys
input = sys.stdin.readline

arr=input().strip()
if arr == '' :
  print(0)
else :
  print(arr.count(' ')+1)