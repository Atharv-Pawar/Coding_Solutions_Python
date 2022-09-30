"""
Chef participated in a contest and got a rank X.

Chef is trying to find his name in the rank-list but there are too many pages.

Each page consists of 25 participants. Chef wants to find the exact page number which contains his name.
Help Chef find the page number.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single integer X - denoting the rank of Chef.
Output Format
For each test case, output the page number of the rank-list containing Chef's name.
"""

T = int(input())
for i in range(T):
    x = int(input())
    print(int(x/25)) if x%25 == 0 else print(int(x/25)+1)