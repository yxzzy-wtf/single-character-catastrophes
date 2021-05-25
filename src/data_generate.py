import random

last = -1

with open("../data.txt", "w") as file:
    for x in range(0, 100000):
        line = [0, 0]
        if last != -1 and random.randint(0, 1) == 0:
            # continue
            line[0] = last
        else:
            line[0] = random.randint(0, 100000)
        line[1] = random.randint(0, 100000)

        file.write(str(line[0]) + " " + str(line[1]) + "\n")


        
