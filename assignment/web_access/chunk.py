import re

chunk = open('./assigment/web_access/chunk.txt', mode='r')
total = None

for line in chunk:
    line = line.rstrip()
    items = re.findall("([0-9]+)", line)

    if len(items) >= 1:
        for value in items:
            value = int(value)

            if total == None:
                total = value
            else:
                total += value

print(total)