import sys
input = sys.stdin.readline

alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()

time = 0

for i in a :
  for j in range(len(alpha)) :
    if i in alpha[j] :
      time += j+3

print(time)