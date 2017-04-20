import random
from datetime import *

file = open("c:\Temp\Snumbers.txt", 'w+')
poem = "I never saw a man who looked\n"
i = 1
#   yherty
while i <= 100:
    numbs = random.sample(range(1, 100), 10)
    sum_stroki = 0
    for item in numbs:
        sum_stroki = sum_stroki + item
    file.write(str(datetime.today()) + '  ' + str(i) + '  ' + str(sum_stroki) + '  ' + str(numbs) + "\n")
    i += 1
file.close()
