import sys
input = sys.stdin.readline

arr =['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input().strip()
count = len(a)

for i in arr :
  count -= a.count(i)
  
print(count)