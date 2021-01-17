"""
1431. Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

:type candies: List[int]
:type extraCandies: int
:rtype: List[bool]
"""
candies = [2,3,5,1,3]
extraCandies = 3
Output = [True,True,True,False,True]

class Solution(object):
    def kidsWithCandies(candies, extraCandies):
        bool_out = []
        
        for n in candies:
            if n + extraCandies >= max(candies):
                bool_out.append(True) 
            else:
                bool_out.append(False)
        print(bool_out)      
        return bool_out


if Solution.kidsWithCandies(candies, extraCandies) == Output:
    print("IT WORKS!!!!!")

else:
    print("Something Went Wrong Here....")


        