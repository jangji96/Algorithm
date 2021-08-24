import sys
input = sys.stdin.readline

a = int(input())
count = 0
if a>=100 :
  for i in range(100,a+1) :
    hun = i % 1000 // 100
    ten = i % 100 // 10
    one = i % 10
    if(i==1000) :
      continue
    if(hun - ten == ten - one) :
      count += 1 
  count+=99
else :
  count+=a
print(count)