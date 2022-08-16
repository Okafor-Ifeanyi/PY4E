# # Prints out available functions of a collection type 
# item = tuple()
# dir(item)

# lst = list()
# dir(lst)

# dic = dict()
# dir(dic)

# ('izu', 'Imbois') > ('izu', 'imboy')

fhand = open('./mbox.txt')
counts = dict()
# This loop seperates the texts in line the words and stores as a Histogam in a dictionary
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst =list()
# This loop gets the value and key from the dictionary and appends it to a list
# for key, value in counts.items():
#     newtub = (value, key)
#     lst.append(newtub)

# # This lis sorts the list usinf the value and reverse the list to start from the highest value
# lst = sorted(lst, reverse=True)

# List Comprehension This replaces line 22 : 29
lst = sorted( [ (value, key) for key, value in counts.items() ], reverse=True)


# This slices the list of the first 10 values and prints key : value (Highest occuring numbers)
for value, key in lst[:10]:
    print(key, value)