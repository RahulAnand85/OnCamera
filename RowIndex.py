d = {}
for row in range(1, int(input())+1):
    r = tuple([int(i) for i in input().split(',')])
    d[row] = r
print(d)