'''
Given two integers dividend and divisor, divide two integers without
using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means 
losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Input
dividend = -1
divisor = -1
Output = -1
Expected = 1



WARNING: NOT EXITING PROPERLY
'''
dividend = -2147483648
divisor = -1

# truncate(3.33333..) = 3.

class Solution(object):
    def divide(self, dividend, divisor):
        run = Solution()
        abs_dividend = abs(dividend)
        counter = 0
        dividend1 = run.scrubber(dividend)
        print(dividend1)
        divisor = run.scrubber(divisor)
        
        while (abs_dividend - abs(divisor)) >= 0:
            counter += 1
            abs_dividend -= abs(divisor)
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            pass
        else:
            counter = (counter - (counter + counter))
        
        run.divide(dividend, divisor)

    def scrubber(self, val):
        if val < -2147483647:
            val = -2147483647
        if val > 2147483647:
            val = 2147483647
        return val

        print(counter)

run = Solution()
run.divide(dividend, divisor)