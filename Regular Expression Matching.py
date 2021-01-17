""" REGULAR EXPRESSION MATCHING

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

Rule 1: '.' Matches any single character.​​​​ (wildcard)
        s = "abc"
        p = "ab."
        MATCH

Rule 2: '*' Matches zero or more of the preceding element.
        s = "abccccccccccccd"
        p = "abc*d"
        MATCH

Rule 3: The matching should cover the entire input string (not partial).
        s = "aa"
        p = "a"
        NO-MATCH

Complete Exampe: 
    s = "mississippi"
    p = "mis*is*p*."    NO-MATCH
    p = "mis*is*ip*."   MATCH
-----------------------------------------------------------------------------

The key here is the star offset. Star creates a condition where the preceeding character in p can be repeated indefinately in s,
and once the repetition is over we need to continue comparing what's left in p with what's left in s, even though the star may have
created a split in our count. We need to track that split between our numbered character lists (dictionary) in order to make sure we're comparing
the appropriate characters with eachother. We will track the offset created by "*" as "star_offset".

It is also important to include a condition for when the star character is a wildcard ".*"

:type s: str
:type p: str
:rtype: bool

Input: s = "mississippi",
    p = "mis*is*p*."    NO-MATCH
    p = "mis*is*ip*."   MATCH

Input: s = "ab" p = ".*" MATCH


LEN p without * == s without star_match_count
"""
#inputs
#s = "mississippi"
#p = "mis*is*p*."   # False
#p = "mis*is*ip*."  # True


s = "aab"
p = "c*a*b" #true

#s = "ab"
#p = ".*" #True

#s = "abcccdzzz"
#p = "abc*dz*"
#s = "abcccccccd"
#p = "abc*d"

#####################################################

class Solution(object):

    def isMatch(self, s, p):
        condition = True
        p_search = {}
        s_set = {}
        p_star_count = 0
        star_offset = 0 # here we store the star-caused offset to use when comparing numbers between p/s.
        star_char = [] # Let's store the last "*"-affected character

        # convert the s and p input lists into dictionary objects.
        for i, c in enumerate(p):
            if c == "*":
               p_star_count += 1
            p_search[i] = c
        for i, c in enumerate(s):
            s_set[i] = c

        # Let's start the search. Here is a shortcut condition for when p has no symbols.
        if "." not in p and "*" not in p:
            if p != s:
                condition = False

        # If there are symbols in p, we're going to compare s and p character by character.
        else:
            for i, c in p_search.items():

                if c != "." and c != "*": #if the character being checked is not a special symbol
                    if c == (s_set.get(i+(star_offset))):
                        condition = True
                    else:
                        print(f"s_set:     {s_set}")
                        print(f"p_search:  {p_search}")
                        return print(f"False! Index Check Failed at {i}:{c} v.s. {i+star_offset}:{s_set.get(i+star_offset)}")

                if c == "*":
                    star_char = p_search.get(i-1) # star_char is the last value before the star.
                    if star_char == ".":
                        cycle_count = 0
                        local_star_offset = 0
                        while (s_set.get(i+local_star_offset, "the_end") != "the_end"): # run wildcard through all the index of s.
                            if cycle_count == 0:
                                cycle_count += 1
                                local_star_offset +=1
                            elif cycle_count > 0:
                                cycle_count += 1
                                local_star_offset +=1
                                star_offset +=1
                        print(f"star index: {i}          local offset: {local_star_offset}          global offset after = {star_offset}")
                        cycle_count = 0
                        local_star_offset = 0 # this needs to reset per use.
                    elif star_char != ".":
                        cycle_count = 0
                        local_star_offset = 0 # God i don't even know how I got here, but this is what we need to do.
                        print(f"\n_______________________________________________________________________________________________________")
                        print(f"                       local offset: {local_star_offset}          global offset before = {star_offset}")
                        while (s_set.get(i+local_star_offset, "the_end") == star_char): # we have to use .get() in order to avoid errors when i not in s_set.
                            if cycle_count == 0:
                                cycle_count += 1
                                local_star_offset +=1
                            elif cycle_count > 0:
                                cycle_count += 1
                                local_star_offset +=1
                                star_offset +=1
                        print(f"star index: {i}          local offset: {local_star_offset}          global offset after = {star_offset}")
                        cycle_count = 0
                        local_star_offset = 0 # this needs to reset per use.
                if c == ".":
                    pass

        # This is where we're making sure all elemnts of s are accounted for in p when adjusting for the star_offset (Rule 3).
        # We're matching adjusted total lengths of a and p to make sure that we're 1:1. Unlike "." which is a wildcard character,
        # "*" is not a character to be compared, but rather an instruction. therefore, we need to subtract the number of "*" in p when
        # we're comparing p and s, since we're only trying to compare character counts.
        """
        if len(s) != (len(p)+(star_offset+1)-p_star_count):
            condition = False
            print(f"False! Failed at length match  p:{len(p)+(star_offset+1)-p_star_count}  v.s.  s:{len(s)}")

        elif len(s) == (len(p)+(star_offset+1)-p_star_count):
            condition = True
            print(f"True!  p:{len(p)+(star_offset+1)-p_star_count}  ==  s:{len(s)}     len(p) = (len(p)+(star_offset+1)-p_star_count)")

        """
        if (len(s)-(star_offset)) != (len(p)):
            condition = False
            print(f"False! Failed at length match  s:{len(s)-(star_offset)}  v.s.  p:{len(p)}")
        
        elif (len(s)-(star_offset)) == (len(p)):
            condition = True
            print(f"True!  s:{len(s)-(star_offset)} == p:{len(p)}")


        print("............................................................................")
        #print(f"star_offset: {star_offset}, p_star_count: {p_star_count}")
        print(condition)
        print(f"s_set:     {s_set}")
        print(f"p_search:  {p_search}")

run = Solution()
run.isMatch(s, p)