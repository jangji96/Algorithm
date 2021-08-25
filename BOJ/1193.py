import sys
input = sys.stdin.readline

a = int(input())
upDown = True
i = 0
stage = 0

while True :
  stage += 1
  i += stage
  upDown = not upDown
  if(i >= a) :
    if(upDown) :
      print('{}/{}'.format(stage-(i-a),1+(i-a)))
    else :
      print('{}/{}'.format(1+(i-a),stage-(i-a)))
    break