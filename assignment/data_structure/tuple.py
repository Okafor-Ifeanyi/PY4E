# This gets the hours in a text and counts them the see the number of transactions that went on per hour
# Reference to tuple.py in ./tutorial/data_structure/tuple.py
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    line = line.split()
    time = line[5]
   # print(time)
    detail = time.split(':')
 	
    hour = detail[0]
    
    counts[hour] = counts.get(hour, 0) + 1
    
#print(counts)
lst = list()

lst = sorted([(key, value) for key, value in counts.items()])

for key, values in lst:
    print(key, values)