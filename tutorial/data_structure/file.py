filename = input('Enter the filename ~ ')

try:
    fhand = open(filename)
except:
    print('File cannot be opened: '+ filename)
    quit()

count = 0

for line in fhand:
    line = line.rstrip()
    # if not line.startswith("text"):
    # if not "oluchi" in line :
    #     continue
    if line.startswith('Subject:'):
        count += 1

print(f"There were {count} 'Subject lines in' {filename}")