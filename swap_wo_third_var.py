x, y = map(int, input().split(' '))
print('X =', x, 'Y =', y)
# print('X =', y, 'Y =', x)
#using modulus operator
if x>y:
    print('X =', y%x, 'Y =', x)
else:
    print('X =', y, 'Y =', x%y)