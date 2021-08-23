import sys
input = sys.stdin.readline

a=int(input())
arr=[]
for i in range(a) :
  arr.append(list(map(int, input().split())))

for i in range(a) :
  print('Case #{}:'.format(i+1),arr[i][0],'+',arr[i][1],'=',arr[i][0]+arr[i][1])