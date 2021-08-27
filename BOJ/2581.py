import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

arr = []
for num in range(a, b+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break 
        if error == 0:
            arr.append(num)
            
if len(arr) > 0 :
    print(sum(arr))
    print(min(arr))
else:
    print(-1)