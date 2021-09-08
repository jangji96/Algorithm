import sys

input = sys.stdin.readline

def distance(s,t,c1,c2):
  # s와 t의 위치에 따라 값이 달라지나, c1과 c2의 위치를 바꿔주면
  # 똑같은 역전의 효과를 낼 수 있다.
  return abs(s-c1)+abs(c1-c2)+abs(t-c2)

def solution(S):
  lastIndex = -1 
  # 단어가 여러개일때 맨 왼쪽부터 맨 오른쪽까지 전부 이동을 해야하므로 양 끝점을 저장한다.
  minIdx = [-1 for _ in range(26)]
  maxIdx = [-1 for _ in range(26)]
  for i in range(26):
    minIdx[i] = S.find(chr(97 + i))
    maxIdx[i] = S.rfind(chr(97 + i))

  # dp배열 선언
  dp = [[0 for _ in range(len(S))] for _ in range(26)]
  
  firstRow = True
  for i in range(26):
    if minIdx[i] == -1:
      continue
    
    # 첫째줄인 경우
    if firstRow:
      for j in range(len(S)):
        dp[i][j] = distance(0, j, minIdx[i], maxIdx[i])
        firstRow = False
        lastIndex = i
      continue

    for j in range(len(S)):
      for k in range(len(S)):
        # 최소거리를 찾음
        minDist = min(distance(k, j, minIdx[i], maxIdx[i]), distance(k, j, maxIdx[i], minIdx[i]))
        # dp배열에 이미 값이 있다면
        if dp[i][j]:
          # 현재 dp[i][j]보다 더 가까운 경로가 있다면 추가해줌
          dp[i][j] = min(dp[i][j], dp[lastIndex][k] + minDist)
        else:
          dp[i][j] = dp[lastIndex][k]+ minDist
    lastIndex = i

  return min(dp[lastIndex]) + len(S)

if __name__ == '__main__':
  S = input()
  S = S[:-1]

  result = solution(S)

  print(result)