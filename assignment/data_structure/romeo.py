# fname = input("Enter your URL ~ ")
fh = open('./assignment/data_structure/romeo.txt')
lst = list()
for line in fh:
    words = line.split()
    # print(words)
    for element in words:
        # print(element)
        if element in lst:
            continue
        else:
            lst.append(element)    

# print(lines)
# lst = lst[0] + lst[1] + lst[2] + lst[3]
lst.sort()
print(lst)
