import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
  n = int(input())
  dic = {}
  result = 1

  for _ in range(n) :
    name,type = map(str, input().split())

    if type in dic :
      dic[type] += 1
    else :
      dic[type] = 1
      
  for i in dic.values():
    result*=i+1
    
  print(result-1)
