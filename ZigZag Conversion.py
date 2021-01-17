"""
Input: s = 'ABCDEFGHIJKLMNOP', numRows = 4
Out: "AGMBFHLNCEIKODJP"

Explanation:
A     G    M    --> AGM
B   F H  L N    --> BFHLN
C E   I K  O    --> CEIKO
D     J    P    --> DJP

AGM + BFHLN + CEIKO + DJP = AGMBFHLNCEIKODJP


Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

RESULTS:
-----------------------------
1157 / 1157 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 13.8 MB

Runtime: 56 ms, faster than 56.86% of Python online submissions for ZigZag Conversion.
Memory Usage: 13.8 MB, less than 5.65% of Python online submissions for ZigZag Conversion.
------------------------------
"""

s = 'ABCDEFGHIJKLMNOP'
numRows = 4


# This is the better method; copied.
class Solution:
    def convert(self, s, numRows):

        counter = 0 # This will track were we are in our oscillating pattern. Starts at zero.
        direction_incriment = 1 # This will determine the direction the counter is going; 1 = forward, -1 = backward.
        output = [""] * numRows # Populate a list with empty entries until its length = numRows.

        for i in range(len(s)):
            output[counter] += s[i] # s[i] is the value attached to the index in "s". Apparently you can do this withuout a dictionary?!
            if numRows > 1:
                counter += direction_incriment # incriment our counter by whatever direction we're currently going.
                if counter == 0 or counter == numRows -1: # If we're at the start or end of the oscillating cycle:
                    direction_incriment *= -1  #this will toggle from positive 1 to negative 1 depending on if we're going forward or backward.
        
        
        # Now let's put together our output string.
        output_string = "" # We start with an emtpy string, and then build the final version by adding to it.
        for j in range(numRows):
            output_string += output[j] # Add the contents of each row to output_string.
        return print(output_string)
        
run = Solution()
run.convert(s, numRows)

"""
# My First Solution

class Solution(object):
    def convert(self, s, numRows):
        list_system = {}
        final_output = []
        last_list = 0
        forward = True

        if numRows == 1:
            list_system[1] = s

        elif numRows != 1:
            # Let's populate our dictionary with empty lists, so we can append them below.
            for n in range(1,numRows+1):
                list_system[n] = []

            # We need the first entry to be counted from 1, not 0 for the math to work. Hence, i+1
            for i, c in enumerate(s):

                # Moving Forward
                if forward == True:
                    if last_list < numRows:
                        last_list += 1
                        list_system[last_list].append(c) 
                    elif last_list == numRows: # End of cycle
                        forward = False
                        last_list -= 1
                        list_system[last_list].append(c) 
                        
                # Moving Backward
                elif forward == False:
                    if last_list > 1:
                        last_list -= 1
                        list_system[last_list].append(c) 
                    elif last_list == 1: # End of cycle
                        forward = True
                        last_list += 1
                        list_system[last_list].append(c) 

        flat_list = []
        # This is how we flatten the dictionary of lists; by appending a new list sub-item by sub-item.
        for i, sublist in list_system.items():
                for item in sublist:
                    flat_list.append(item)
        blank = ""
        final_output = blank.join(flat_list)
        print(final_output)
        
run = Solution()
run.convert(s, numRows)
"""