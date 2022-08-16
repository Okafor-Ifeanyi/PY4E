name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()

for line in handle: 
    if not line.startswith('From '):
        continue
        
    line = line.split()
    word = line[1]
    emails[word] = emails.get(word,0) + 1

bigword = None
bigcount = None

for word, count in emails.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)