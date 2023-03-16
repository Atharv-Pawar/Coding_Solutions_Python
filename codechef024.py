"""
Once, after a stressful day, Chef decided to relax and visit a casino near his house to gamble. He feels lucky and he's going to bet almost all of his money.

The game Chef is going to play in the casino consists of tossing a die with
�
N faces twice. There is a number written on each face of the die (these numbers are not necessarily distinct). In order to win, Chef must get the number
�
A on the first toss and the number
�
B on the second toss of the die.

The excited viewers want to know the probability that Chef will win the game. Can you help them find that number? Assume that Chef gets each face of the die with the same probability on each toss and that tosses are mutually independent.

Input
The first line of the input contains a single integer
�
T denoting the number of test cases. The description of
�
T test cases follows.
The first line of each test case contains three space-separated integers
�
N,
�
A and
�
B.
The second line contains
�
N space-separated integers
�
1
,
�
2
,
…
,
�
�
x
1
​
 ,x
2
​
 ,…,x
N
​
  denoting the numbers written on the faces of the die.
Output
For each test case, print a single line containing one real number — the probability that Chef will win. Your answer will be considered correct if its absolute error does not exceed
1
0
−
6
10
−6
 .
"""
T = int(input())
if 1<=T<=70:
    for i in range(T):
        N, A, B = map(int, input().split())
        x = list(map(int, input().split()))[:N]
        if T<=10 and 1<=N<=100 and 1<=A<=N and 1<=B<=N:
            p1 = x.count(A)/N
            p2 = x.count(B)/N
            print(p1*p2)
        else:
            print("Invalid Input")
else:
    print("Invalid Test Case")