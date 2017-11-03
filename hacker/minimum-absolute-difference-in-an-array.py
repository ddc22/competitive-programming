import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here
min = 10000000000
for index1 in range(len(a)):
    for index2 in range(index1+1, len(a)):
        diff = abs(a[index1] - a[index2])
        if(diff < min):
            min = diff
print min