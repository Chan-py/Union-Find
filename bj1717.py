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
    if par[a] > par[b]:
        a, b = b, a
    
    if a != b:
        par[b] = a
        return True
    else:
        return False

n, m = map(int, input().split())
par = [-1 for _ in range(n+1)]
for _ in range(m):
    key, a, b = map(int, input().split())
    if key == 0:
        merge(a, b)
    elif key == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")