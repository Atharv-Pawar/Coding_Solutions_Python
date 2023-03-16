"""
In Byteland they have a very strange monetary system.

Each Bytelandian gold coin has an integer number written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers are all rounded down (the banks have to make a profit).

You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins.

You have one gold coin. What is the maximum amount of American dollars you can get for it?

Input Format
The input will contain several test cases (not more than 10).
Each testcase is a single line with a number n, it is the number written on your coin.

Output Format
For each test case output a single line, containing the maximum amount of American dollars you can make.

Constraints
0 \leq n \leq 10^90≤n≤10
9
"""
d = dict()


def cal(n):
    if n <= 10:
        return n
    if n in d:
        return d[n]
    d[n] = max(n, cal(n // 2) + cal(n // 3) + cal(n // 4))
    return d[n]


while True:
    try:
        n = int(input())
        print(cal(n))
    except:
        break