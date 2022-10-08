"""
Mario transforms each time he eats a mushroom as follows:

If he is currently small, he turns normal.
If he is currently normal, he turns huge.
If he is currently huge, he turns small.
Given that Mario was initially normal, find his size after eating X mushrooms.

Input Format
The first line of input will contain one integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, containing one integer X.
Output Format
For each test case, output in a single line Mario's size after eating X mushrooms.

Print:

NORMAL, if his final size is normal.
HUGE, if his final size is huge.
SMALL, if his final size is small.
You may print each character of the answer in either uppercase or lowercase (for example, the strings Huge, hUgE,huge and HUGE will all be treated as identical).
"""
t = int(input())
for _ in range(t):
    lst = ['NORMAL', 'HUGE', 'SMALL']
    x = int(input())
    if x%3 == 0:
        print(lst[0])
    if x%3 == 1:
        print(lst[1])
    if x%3 == 2:
        print(lst[2])