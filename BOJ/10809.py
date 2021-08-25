import sys
input = sys.stdin.readline

arr=input()
for i in range(ord('a'),ord('z')+1) :
  if chr(i) in arr :
    print(arr.index(chr(i)))
  else :
    print(-1)