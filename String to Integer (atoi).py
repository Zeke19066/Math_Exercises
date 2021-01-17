"""
:type s: str
:rtype: int

Input
"   +0 123" = 0
"s = "-000000000000001" =-1
Output
123
Expected
0

RESULTS
------------------------------------
Efficient Ver2:

1084 / 1084 test cases passed.
Status: Accepted
Runtime: 20 ms
Memory Usage: 13.5 MB
Runtime: 20 ms, faster than 82.99% of Python online submissions for String to Integer (atoi).
Memory Usage: 13.5 MB, less than 48.46% of Python online submissions for String to Integer (atoi).

_________________
Inefficient Ver1:
if c != " " and c != "+" and c != "-" and c != "0": # if c is not an symbol or zero: #this logic condition slowed down the process.

1084 / 1084 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 13.5 MB
Runtime: 28 ms, faster than 38.20% of Python online submissions for String to Integer (atoi).
Memory Usage: 13.5 MB, less than 46.29% of Python online submissions for String to Integer (atoi).
"""

s = "4193with words"

class Solution(object):
    def myAtoi(self, s):
        program = Solution()
        special_characters = [" ", "+", "-", "0"]
        intial_output = []
        final_output = 0
        admissions_counter = 0 # How many c have been allowed past the gates?!
        knight_counter = 0 # How many symbols have been allowed past the gates?!
        early_zero = 0 # the zeros if they arrive before the others

        print(f"Over the hills, ___|{s}|___ approach the castle gates.")
        for c in str(s):
            if c not in special_characters: # if c is not an symbol or zero:
                if c.isdigit() == True: # This is how we check if c is a number.
                    intial_output.append(str(c)) # If f they pass the 'int()' oath, they shall be admitted by name.
                    print(f'Noble {c}, the castle welcomes you! {len(intial_output)}')
                    admissions_counter += 1 # Note it in the guest-counter
                elif c.isdigit() != True:
                    print(f"Traitor Found! {c} is no Noble Figure! CLOSE THE GATE!!!")
                    return program.scrubber(intial_output)
            if c == "0":
                if admissions_counter != 0: # Let them in! An int has passed by! 
                    print(f"Let {c} through, the Nobles are in the keep")
                    admissions_counter += 1 # Note it in the guest-counter
                    intial_output.append(str(0)) # Add them to the guestbook, general stamp will do
                if admissions_counter == 0 and knight_counter == 0: # just a local, ignore
                    print(f'A lowly {c} is ahead! hope no Knights follow!')
                    early_zero += 1
            if c == " ":
                if len(intial_output) > 0 or early_zero > 0:
                    print(f"A sheep interrupts the procession! CLOSE THE GATE!!!")
                    return program.scrubber(intial_output)
            if c == "+" or c == "-":
                if len(intial_output) > 0 or early_zero > 0 or knight_counter > 0:
                    print(f"The coward knight ({c}) arrives after the others! CLOSE THE GATE!!!")
                    return program.scrubber(intial_output)
                if len(intial_output) == 0 and early_zero == 0:
                    print(f"The Vanguard knight apporaches! Let ({c}) through!")
                    knight_counter += 1
                    intial_output.append(c) # Add them to the guestbook
        return program.scrubber(intial_output)

    def scrubber(self, intial_output):
        if len(intial_output) == 0: #intial_output figure cannot be blank.
            intial_output = [str(0)]
        if len(intial_output) == 1:
            if "-" in intial_output or "+" in intial_output: #intial_output figure cannot be a lone symbol.
                intial_output = [str(0)]
        blank = ""
        final_output = int(blank.join(intial_output))
        print("********* GAME OVER ************")
        if final_output < -2147483648:
            print(f'Woah there ___|{final_output}|___ , yee be too low!')
            final_output = -2147483648
        if final_output > 2147483647:
            print(f'Woah there ___|{final_output}|___ , no giants allowed!')
            final_output = 2147483647
        print(f"FINAL OUTPUT: {final_output}")
        return final_output

program = Solution()
program.myAtoi(s)