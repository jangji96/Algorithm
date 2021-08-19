'''
예제 입력 1 
2000

예제 출력 1 
1

예제 입력 2 
1999

예제 출력 2 
0
'''
a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print(1)
else:
    print(0)