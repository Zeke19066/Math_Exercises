"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
s = 'ABCDEFGHIJKLMNOP'
numRows = 4
list_system = {}
final_output = []
forward = TRUE

class Solution(object):
    def convert(self, s, numRows):
        for i, c in enumerate(s):
        # We need the first entry to be counted from 1, not 0 for the math to work. Hence, i+1

            # Moving Forward
            if forward == True:
                if (i+1) % numRows == 0: # If the remainder of the index/numRows is zero (its divisible by numRows), put it in the numRows (last) list
                    if list_system.get(numRows, "error") == "error":
                        list_system[numRows] = [] # throw an emtpy list for our last list.
                    list_system[numRows].append(c) # New entry = Old entry + "c"
                    forward = False # we've completed a cycle, let's flip the toggle.
                    print(f' i = {i}, c = {c}, MOD = {(i+1) % numRows}')

                if (i+1) % numRows != 0: # If the remainder of the index/numRows is not zero, add "c" to the remainder dictoinary entry.
                    if list_system.get(((i+1) % numRows), "error") == "error":
                        list_system[((i+1) % numRows)] = [] # throw an emtpy list for our last list.
                    list_system[(i+1) % numRows].append(c) # New entry = Old entry + "c"
                    print(f' i = {i}, c = {c}, MOD = {(i+1) % numRows}')


            # Moving Backward
            if forward == False:
                if (i+1) % numRows == 0: # If the remainder of the index/numRows is zero (its divisible by numRows), put it in the numRows (last) list
                    if list_system.get(numRows, "error") == "error":
                        list_system[numRows] = [] # throw an emtpy list for our last list.
                    list_system[numRows].append(c) # New entry = Old entry + "c"
                    forward = True # we've completed a cycle, let's flip the toggle.
                    print(f' i = {i}, c = {c}, MOD = {(i+1) % numRows}')

                if (i+1) % numRows != 0: # If the remainder of the index/numRows is not zero, add "c" to the remainder dictoinary entry.
                    if list_system.get(((i+1) % numRows), "error") == "error":
                        list_system[((i+1) % numRows)] = [] # throw an emtpy list for our last list.
                    list_system[(i+1) % numRows].append(c) # New entry = Old entry + "c"
                    print(f' i = {i}, c = {c}, MOD = {(i+1) % numRows}')


            
        
        print(list_system)
        flat_list = []
        for sublist in list_system:
                flat_list.append(sublist)
        blank = ""
        final_output = int(blank.join(flat_list))
        print(final_output)

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
run = Solution()
run.convert(s, numRows)