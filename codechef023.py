"""
Problem
Chef has a string
�
S with him. Chef is happy if the string contains a contiguous substring of length strictly greater than
2
2 in which all its characters are vowels.

Determine whether Chef is happy or not.

Note that, in english alphabet, vowels are a, e, i, o, and u.

Input Format
First line will contain
�
T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, a string
�
S.
Output Format
For each test case, if Chef is happy, print HAPPY else print SAD.

You may print each character of the string in uppercase or lowercase (for example, the strings hAppY, Happy, haPpY, and HAPPY will all be treated as identical).

Constraints
1
≤
�
≤
1000
1≤T≤1000
3
≤
∣
�
∣
≤
1000
3≤∣S∣≤1000, where
∣
�
∣
∣S∣ is the length of
�
S.
�
S will only contain lowercase English letters.
"""
t = int(input())
for i in range(t):
    S=input()
    string="not contiguous"
    vowels=['a','e','i','o','u']
    for i in range(len(S)-3):
        if (S[i] in vowels) and (S[i+1] in vowels) and (S[i+2] in vowels):
            string="contiguous"
            print("Happy")
            break
    if string!="contiguous":
        print("Sad")