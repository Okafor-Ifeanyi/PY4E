

# The code below runs through a  bunch of texts and picks any 
# line starting with "X_DSPAM...", gets the digit behind it 
# sums it up and divideds it by the total number to get the average
 
fname = input("Enter file name: ")
fh = open(fname)
score = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    score = score + float(line[20:])
    
    
average = score/count
print(f"Average spam confidence: {average}")