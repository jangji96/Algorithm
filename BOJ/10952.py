import sys
input = sys.stdin.readline

arr=[]
i = 0
while True :
  arr.append(list(map(int, input().split())))
  if arr[i][0]+arr[i][1]==0 :
    break
  print(arr[i][0]+arr[i][1])
  i += 1
  