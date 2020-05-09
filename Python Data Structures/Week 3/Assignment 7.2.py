'''
Write a program that prompts for a file name,
then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values
from each of the lines and compute the average of those
values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
'''
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
count = 0
tot = 0
ans = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line.rstrip()
    count = count + 1
    num = float(line[20:])
    tot = num + tot
ans = tot / count
print ("Average spam confidence:", ans)
