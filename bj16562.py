import sys
input = sys.stdin.readline

def find(x):
    if par[x] == -1:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def merge(a, b):
    a = find(a)
    b = find(b)
    if v[a] > v[b]:
        a, b = b, a
    
    if a != b:
        par[b] = a
        return True
    else:
        return False

N, M, K = map(int, input().split())
par = [-1 for _ in range(N+1)]
v = [0] + list(map(int, input().split()))
for _ in range(M):
    a, b = map(int, input().split())
    merge(a, b)
sum = 0
for i in range(1, N+1):
	if par[i] == -1:
		sum += v[i]
if sum > K:
	print("Oh no")
else:
	print(sum)