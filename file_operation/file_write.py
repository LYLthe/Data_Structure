"""
write an integer from 1 to 500 to a folder,
if the folder exist,write directly
else,create a new folder and write
"""


import random
with open('integers.txt', 'w') as f:
    for count in range(500):
        number = random.randint(1, 500)
        f.write(str(number) + '\n')
