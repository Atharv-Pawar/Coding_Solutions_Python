if __name__ == "__main__":
    k = int(input('Enter a number'))
    for i in range(1, k):
        b = str(bin(i))[2:]
        o = str(oct(i))[2:]
        h = str(hex(i))[2:]
        h = h.upper()
        print(b, o, i, h)