'''
예제 입력 1 
10 10

예제 출력 1 
9 25

예제 입력 2 
0 30

예제 출력 2 
23 45
'''
# solution1
a, b = map(int, input().split())
if b>=45 :
  print(a, b-45)
else :
  if a == 0 :
    print(23, b+60-45)
  else :
    print(a-1, b+60-45)
    
# solution2
a,b=map(int,input().split())
c=60*a+b
print(((c-45)//60)%24,(c-45)%60)