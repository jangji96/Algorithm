import sys
input = sys.stdin.readline

while True :
  n = input().strip()
  if n == '0' :
    break
  tf = True
  for i in range(len(n)//2):
    if n[i] != n[len(n)-1-i] :
      tf=False
  if tf :
    print('yes')
  else :
    print('no')