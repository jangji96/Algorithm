import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
matrix = [] 
result = [0, 0, 0] 

for _ in range(N): 
  matrix.append(list(map(int, sys.stdin.readline().split())))

minus = 0
zero = 0
plus = 0

def counting(x, y, n):
  global minus, zero, plus
  
  keyNum = matrix[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if(matrix[i][j] != keyNum):
        for k in range(3):
          for l in range(3):
            counting(x + k * n//3, y + l * n//3, n//3)
        return
          
  if(keyNum == -1):
    minus += 1
  elif(keyNum == 0):
    zero += 1
  else:
    plus += 1
        
counting(0, 0, N)

print(minus)
print(zero)
print(plus)