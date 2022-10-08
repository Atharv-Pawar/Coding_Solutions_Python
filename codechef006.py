"""
You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A, T, C,and G only.

Chef knows that:

A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string SS, determine the sequence of the complementary strand of the DNA.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case contains an integer N - denoting the length of string S.
Second line contains N characters denoting the string S.
Output Format
For each test case, output the string containing NN characters - sequence of nucleotides of the complementary strand.
"""

"""
Input                          Output
4                              TAGC                       
4                              CAGG
ATCG                           TTTTT   
4                              ATG
GTCC
5
AAAAA
3
TAC
"""


# cook your dish here
def DNAstrand(n, s):
    finalStrand = ""
    for i in range(n):
        if s[i] == 'A':
            finalStrand += 'T'
        if s[i] == 'T':
            finalStrand += 'A'
        if s[i] == 'C':
            finalStrand += 'G'
        if s[i] == 'G':
            finalStrand += 'C'

    return finalStrand


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(DNAstrand(n, s))
