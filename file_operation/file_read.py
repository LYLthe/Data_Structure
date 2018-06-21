"""
open a file and read all integers
calculate their sum
"""


with open('integers.txt', 'r') as f:
    sumsum = 0
    for line in f:
        line = line.strip()
        number = int(line)
        # print(number)
        sumsum += number
    print('sum is : ', sumsum)
