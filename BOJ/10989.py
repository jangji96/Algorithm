import sys
input = sys.stdin.readline

sArr = [0]

for _ in range(10000) :
  sArr.append(0)

N = int(input())

for _ in range(N) :
  num = int(input())
  sArr[num] += 1

for i in range(len(sArr)) :
  if sArr[i] != 0 :
    for _ in range(sArr[i]) :
      print(i)