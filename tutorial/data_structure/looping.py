fruit = "banaanananananananananananna"
count = 0

for items in fruit:
    if items == 'b':
        count += 1

print(count)

# Logical Operator
if "a" in fruit:
    print("Found It")

print(fruit.upper())
print(fruit.title())

print(fruit.find('a'))