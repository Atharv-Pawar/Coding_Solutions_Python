"""
Two integers A and B are the inputs. Write a program to find GCD and LCM of A and B.

Input Format
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer A and B.

Output Format
Display the GCD and LCM of A and B separated by space respectively. The answer for each test case must be displayed in a new line.
"""

"""
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    gcd, lcm = 0, 0
    for i in range(a):
        for j in range(b):
            d = max(i, j, 1)
            if a%d==0 and b%d==0:
                gcd = d
            lcm = a*b//gcd
    print(gcd, lcm)
"""

# the above program exceeded the time limit

def gcd(x, y):
    while y>0:
        x, y = y, x % y
    return x


def lcm(x, y):
    l = (x * y) // gcd(x, y)
    return l


T = int(input())
for i in range(T):
    (a, b) = map(int, input().split(' '))
    print(gcd(a, b), lcm(a, b))