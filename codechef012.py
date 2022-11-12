"""
There is a grid of size 10^5×10^5
 , covered completely in railway tracks. Tom is riding in a train, currently in cell (a,b), and Jerry is tied up in a different cell (c,d), unable to move. The train has no breaks. It shall move exactly K steps, and then its fuel will run out and it shall stop. In one step, the train must move to one of its neighboring cells, sharing a side. Tom can’t move without the train, as the grid is covered in tracks. Can Tom reach Jerry’s cell after exactly K steps?

Note: Tom can go back to the same cell multiple times.

###Input

The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, five integers a,b,c,d,K.
###Output For each testcase, output in a single line "YES" if Tom can reach Jerry's cell in exactly KK moves and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
"""

T = int(input())
if 1<=T<=(10**5):
    for _ in range(T):
        a, b, c, d, k = map(int, input().split())
        if 0<=a<=(10**5) and 0<=b<=(10**5) and 0<=c<=(10**5) and 0<=d<=(10**5) and (a != c or b != d) and 1<=k<=(2*10**5):
            result = abs(c-a) + abs(d-b)
            if result==k:
                print('YES')
            elif k>result:
                if (k-result)%2==0:
                    print('YES')
                elif (k-result)%2==1:
                    print('NO')
            else:
                print('NO')
        else:
            print('Invalid Inputs')
else:
    print('Invalid Inputs')