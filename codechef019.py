"""
Problem
A football league of N teams is taking place, where each team plays other teams once in single round robin fashion<Wikipedia>. A team gets 3 points for winning a game and 0 for losing (assume that no games end in a draw/tie). What is the maximum possible difference of points between the winning team and the second-placed team?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing a single integer N.
Output Format
For each test case, output in a single line the maximum difference of points between first and second place.
"""
for _ in range(int(input())):
    n = int(input())
    print((n//2)*3) #logic