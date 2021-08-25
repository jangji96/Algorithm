import sys
input = sys.stdin.readline

up,down,high = map(int, input().split())
day = (high-(up-(up-down))) // (up-down)
if (high-(up-(up-down))) % (up-down) != 0 :
  day += 1
print(day)