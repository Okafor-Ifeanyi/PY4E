import re

x = "From: Hail mary full of grace the 30 lord is with thee : blessed are you 2j5 amongst  678 and blessed : is the fruit 9 of your womb Jesus   "
z = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# y = re.findall('[0-9]+', x) # find all integers
# y = re.findall('^F.+:', x) # find longest char that start with F ends with :
# y = re.findall('lo.+?:', x) # find the shortest match to "lo .... : "
y = re.findall('\S+?@\S+', z) # finding all char with @ inclusive
print(y)


atops = z.find('@')
print(atops)

sppos = z.find(' ', atops)
print(sppos)

host = z[atops+1 : sppos]
print(host)

words = z.split()
email = words[1]
pieces = email.split('@')
print(pieces[0])