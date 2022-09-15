def print_formatted(number):
    # your code goes here
    binlen = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(int(i)).rjust(binlen), oct(i)[2:].rjust(binlen), hex(i)[2:].rjust(binlen).upper(),
              bin(i)[2:].rjust(binlen))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)