"""
Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

:type s: str
:rtype: int

the trick here: as we scan, if the new char is already in ls, then remove the existing diplicate and everything that came before it,
then append the ls with the new char and continue.
"""
#s = "pwwkew"
s = "dvdf"
output = 3
######################

ls = []
maxlen = 0

for i, c in enumerate(s):
    if c not in ls:
        ls.append(c)
        if len(ls) > maxlen:
            maxlen = len(ls)
    elif c in ls:
        ls = ls[ls.index(c)+1:] #this is the key here.
        ls.append(c)

print(maxlen)