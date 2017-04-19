import random
file = open("c:\Temp\Snumbers.txt", 'w+')
poem = "I never saw a man who looked\n"
i=0

while i<=1000:
    numbs = random.sample(range(1, 1000), 10)
    file.write(str(numbs)+"\n")
    i+=1

file.close()
