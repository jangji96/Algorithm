'''
예제 입력 1 
1 2
예제 출력 1 
<

예제 입력 2 
10 2
예제 출력 2 
>

예제 입력 3 
5 5
예제 출력 3 
==
'''
a, b = map(int, input().split())
if a>b :
  print('>')
elif a==b :
  print('==')
else :
  print('<')