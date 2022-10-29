"""
Chef and Chefina are residing in a hotel.

There are 10 floors in the hotel and each floor consists of 10 rooms.

Floor 1 consists of room numbers 1 to 10.
Floor 2 consists of room numbers 11 to 20.
…
Floor i consists of room numbers 10 .(i-1) + 1 to 10 . i.
You know that Chef's room number is X while Chefina's Room number is Y.
If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X,Y, the room numbers of Chef and Chefina respectively.
Output Format
For each test case, output the number of floors Chef needs to travel to reach Chefina's room.
"""
"""
Inputs                    Outputs
4                         9
1 100                     0
42 50                     3
53 30                     1
81 80
"""
# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split(' '))
    s_floor = int((x-1)/10) #logic 1
    e_floor = int((y-1)/10) #logic 2
    print(abs(e_floor - s_floor)) #final-logic