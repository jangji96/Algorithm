import sys
input = sys.stdin.readline

arr=input().upper().strip()
count = [0 for _ in range(26)]

for i in arr :
  count[ord(i)-97+32] += 1

if count.count(max(count)) > 1 : 
  print('?')
else :
  print(chr(count.index(max(count))+97-32))