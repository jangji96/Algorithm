a=int(input())
arr=[]
for i in range(a) :
  arr.append(list(map(int, input().split())))

for i in range(a) :
  print(arr[i][0]+arr[i][1])