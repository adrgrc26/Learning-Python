#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

s = []
for t in sys.argv[1:]:
	s.append(float(t))
s.sort()


count = 0
for i in range(len(s)):
	count += 1


sum = 0
for i in range(len(s)):
	sum += s[i]
	mean = sum/count


x = 0
for j in range(len(s)):
	x += (s[j] -mean) ** 2

y = math.sqrt(x/count)



a = int(count/2)
b = int((count-1)/ 2)
med = (s[a] + s[b]) /2

#print time
print(count)
print(s[0])
print(s[-1])
print('%.3f' %(y))
print('%.3f' %(mean))
print ('%.3f' %(med))
"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
