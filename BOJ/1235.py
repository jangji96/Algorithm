n = int(input()) 
arr = []
lenth=1
tenten=10

for _ in range(n):
  arr.append(int(input()))

while True :
  index = 0
  newArr = arr[:] # 초기 입력받은 배열로 초기화

  # 낮은 자릿수 부터 동일한 번호가 있는지 비교하기 위해  새로운 배열 생성
  for i in arr :
    newArr[index] = i % tenten
    index = index + 1
  
  # set 자료형은 중복을 제거함
  # 중복을 제거한 배열의 길이가 원래 배열의 길이보다 짧다면 중복되는 값 있음
  if(len(set(newArr)) < len(arr)) :
    tenten = tenten * 10 # tenten으로 나눈 나머지 자릿수 증가
    lenth=lenth+1
  else :
    break

print(lenth)