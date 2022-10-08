# Factorial calculation using function
def fact(n):
    if n==0:
        res = 1
    res = 1
    for i in range(1, n+1):
        res = res*i
    return res

if __name__=="__main__":
    x = int(input())
    print(fact(x))