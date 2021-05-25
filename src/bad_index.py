# read file of numbers in lines A B
# print out all numbers where A is larger than last line's B, and print the sum

map_step = {}
file = open("../data.txt")

last = 9999999
total = 0

for line in file.readlines():
    items = line.split(' ')
    if last < int(items[0].rstrip()):
        total += int(items[0])
        print(items[0])
    last = int(items[0].rstrip()) # 1 changed to 0
print("total: " + str(total))