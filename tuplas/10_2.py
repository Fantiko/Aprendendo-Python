# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

fh = open('mbox-short.txt')
dicio = dict()

for line in fh:
    line.rstrip()
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    hora = words[5].split(':')
    dicio[hora[0]] = dicio.get(hora[0], 0) + 1
for key, value in sorted(dicio.items()):
    print(key, value)
