import sys
input = sys.stdin.readline

a = int(input())
arr =[]
count = 0

for _ in range(a) :
  arr.append(list(map(int,input().split())))

for i in range(a) :
  for j in range(1,arr[i][0]+1):
    if ((sum(arr[i]) - arr[i][0]) / arr[i][0]) < arr[i][j] : 
      count += 1
  print('%.3f'%(count / arr[i][0] * 100)+'%')
  count = 0