#!/usr/bin/python

import sys

list1 = []

f1 = open(sys.argv[1], "r")
for line in f1:
    for word in line.split():
        list1.append(word)
f1.close()

print "list1 is: ", list1

list1Length = len(list1)
print "list1Lenth: ", list1Length


list2 = []

f2 = open(sys.argv[2], "r")
for line in f2:
    for word in line.split():
        list2.append(word)
f2.close()

print "list2 is: ", list2

list2Length = len(list2)
print "list2Length: ", list2Length

outLength = list1Length + list2Length
out = [None] * outLength

if (list1 == [] or list2 == []):
    print "Empty List"
else:

    list1_rev = []
    for i in range((list1Length-1),-1,-1):
        list1_rev.append(list1[i])

    list2_rev = []
    for i in range((list2Length-1),-1,-1):
        list2_rev.append(list2[i])

    print list1_rev
    print list2_rev
        
    for i in range(0,(list1Length),1):
        out[(i*2)] = list1_rev[i]

    for i in range(0,list2Length,1):
        out[((i*2)+1)] = list2_rev[i]

    print "The list out is: ", out

    f3 = open("output.txt", "w")
    for i in out:
        f3.write(i)
        f3.write(" ")

    


