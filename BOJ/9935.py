import sys
input = sys.stdin.readline

string = list(input().strip())
bangStr = list(input().strip())
bangStr = bangStr[::-1]
check = True
# sub = 0
# cnt = 0
# for i in range(len(bangStr)-1,len(string))  :
#   sub=0
#   if string[i] == bangStr[0] :
#     check = True
#     for j in range(len(bangStr)) :
#       while string[i-j-sub] == '' :
#         sub +=1
#       if bangStr[j] != string[i-j-sub] :
#         check = False
#         break;
#     if check == True :
#       for k in range(i-j-sub,i+1) : 
#         string[k] = ''


# for i in string :
#   if i != '' :
#     print(i,end='')
#   else :
#     cnt+=1 

# if cnt == len(string) :
#   print('FRULA')

arr=[]

for i in range(len(string)) :
  arr.append(string[i])
  if string[i] == bangStr[0] :
    check = True
    for j in range(len(bangStr)) :
      if bangStr[j] != arr[len(arr)-1-j] :
        check = False
        break;
    if check == True :
      for _ in range(len(bangStr)) :
        arr.pop()
if len(arr) == 0 :
  print('FRULA')
else :
  for i in arr :
    print(i,end='')