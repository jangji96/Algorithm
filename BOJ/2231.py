import sys
input = sys.stdin.readline

n = int(input())
result = 0
for i in range(1, n+1):
    arr = list(map(int, str(i)))
    sumArr = i + sum(arr)
    if(sumArr == n):
        result = i
        break
print(result)