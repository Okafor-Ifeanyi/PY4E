import re 

lin = "From biopython@gmail.com Sat jun 5 09:14:16 2008"
y = re.findall('@([^ ]*)', lin)
y = re.findall('^From .*@([^ ]*)', lin)

print(y)