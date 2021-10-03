t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    owner = []

    for _ in range(n+1) :
      owner.append(False)

    arr = []

    for _ in range(m):
      arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: x[1])

    cnt = 0
    for i in arr :
      a, b = i[0], i[1]

      for i in range(a, b+1):
        if not owner[i]:
          cnt += 1
          owner[i] = True
          break

    print(cnt)