# Playing with match-sticks
# cook your dish here
# z, o, t, th, f, fi, s, sv, e, n = 6, 2, 5, 5, 4, 5, 6, 3, 7, 6
for _ in range(int(input())):
    a, b = map(int, input().split())
    result = a+b
    d = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    c_mstick = 0
    for i in str(result):
        c_mstick += d[int(i)]
    print(c_mstick) 
