import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):  
    floor = int(input())
    num = int(input())
    arr = [1 for _ in range(1, num+1)]

    for _ in range(floor+1) :
        for i in range(1,num) :
            arr[i] += arr[i-1]
    print(arr[-1])