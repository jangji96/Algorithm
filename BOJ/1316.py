import sys
input = sys.stdin.readline

a = int(input())
string = []
tfArr= []
change = False 
count = 0

for _ in range(a) :
  tfArr= [False for _ in range(26)]
  string = input()
  count += 1
  for i in range(len(string)-1) :
    if(string[i] != string[i+1]) :
      if(tfArr[ord(string[i])-97] == True) :
        count -=1
        break
      else :
        tfArr[ord(string[i])-97] = True

print(count)
