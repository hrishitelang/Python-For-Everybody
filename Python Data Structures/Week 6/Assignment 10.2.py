'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line  = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        x = words[5].split(':')
        print(x[0])
        d[x[0]] = d.get(x[0],0) + 1
print (d)
l = []
for k,v in d.items():
    l.append((k,v))

print (l)
l = sorted(l)
for k,v in l:
    print (k,v)
