#!/bin/python3

# Solution for: https://www.hackerrank.com/contests/pride-ab-filtering-test-3rd-years/challenges/two-characters

import sys

# Checks if given str is valid string t (check problem statement)
def isValidStr(str, c1, c2):
	
	char2_str = str[0::2];
	char1_str = str[1::2];

	if char1_str[0] == c1:
		return (char1_str.count(c1) + char2_str.count(c2)) == len(str);
	else:
		return (char1_str.count(c2) + char2_str.count(c1)) == len(str);



s_len = int(input().strip())
s = str(input().strip())


chars_in_s = [];
# find all distinct characters in the input string
for c in s:
	if chars_in_s.count(c) == 0:
		chars_in_s.append(c);

max = 0;
# choose two distinct characters
# keep only these two in the string
# and check if we get a valid string t
for c1 in range(0, len(chars_in_s)):
	for c2 in range(c1+1, len(chars_in_s)):
		newstr = [];
		for i in s:
			if i == chars_in_s[c1] or i == chars_in_s[c2]:
				newstr.append(i);
		if isValidStr(newstr, newstr[0], newstr[1]) and len(newstr) >= max:
			max = len(newstr);
print(max);

		
