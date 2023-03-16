"""
Make A and B equal
Chef has two numbers A and B.

In one operation, Chef can choose either A or B and multiply it by 2.

Determine whether he can make both A and B equal after any number (possibly, zero) of moves.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers A and B.
Output Format
For each test case, output YES if Chef can make both numbers equal, NO otherwise.

Note that the checker is case-insensitive i.e. YES, Yes, yes, yES are all considered same.
"""
for _ in range(int(input())):
    a, b = map(int, input().split())
    flag = 0
    if a == b:
        flag = 1
    elif a > b :
        while a >= b :
            if a == b :
                flag = 1
            b *= 2
    else :
        while a <= b :
            if a == b :
                flag = 1
            a *= 2
    if flag == 1 :
        print('yes')
    else :
        print('no')