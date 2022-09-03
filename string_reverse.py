def rev_string(S):
    return S[::-1]


# def palindrome(name):
#     ob = rev_string(name)
#     if ob == name:
#         return 1
#     return 0


if __name__ == "__main__":
    userResponse = input('Enter the word')
    print(rev_string(userResponse))