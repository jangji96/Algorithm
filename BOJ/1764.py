import sys
input = sys.stdin.readline

N, M = map(int, input().split())
listen = [input().strip() for _ in range(N)]
see = [input().strip() for _ in range(M)]

seeListen = list(set(listen) & set(see))

seeListen.sort()

print(len(seeListen))
for i in seeListen:
    print(i)