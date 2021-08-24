import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int,input().split()))

arr.sort()

print(arr[0],arr[a-1])