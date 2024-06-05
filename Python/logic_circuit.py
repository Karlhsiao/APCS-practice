p, q, r, m = map(int, input().split())


for i in range(p):
    nodes = {"name": i, "type": "in", "out": [], "in": []}


for i in range(p, p+q):
    nodes = {"name": i, "type": "in", "out": [], "in": []}


for i in range(p+q, p+q+r):
    nodes = {"name": i, "type": "in", "out": [], "in": []}