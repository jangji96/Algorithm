arr = list(map(int,input().split()))
origin = arr[:]
arr.sort()
sortArr = arr[:]
arr.sort(reverse=True)
reverseArr = arr[:]
if origin == sortArr :
  print('ascending')
elif origin == reverseArr :
  print('descending')
else :
  print('mixed')