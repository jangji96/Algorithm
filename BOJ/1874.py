import sys
input = sys.stdin.readline

n = int(input())
result = []
stack = []

num = 0

possible = True

for _ in range(0,n) :
  i = int(input())

  while num < i :
    num +=1
    stack.append(num)
    result.append("+")

  if stack[-1]==i:
    stack.pop()
    result.append("-")
  else:
    possible = False

if possible :
  for i in result :
    print(i)
else :
  print('NO')
