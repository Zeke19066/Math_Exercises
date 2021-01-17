
#height = [0,1,0,2,1,0,1,3,2,1,2,1]  #Sorted_height = [3, 2, 1, 0]
#height = [4,2,0,3,2,5] #Sorted_height = [5, 4, 3, 2, 0]
height = [2,0,2]
#height = []

#TOO SLOW

class Solution(object):
    def trap(self, height):
        water_counter = 0 # these are moving counters used in the algorithm.

        if height == []:
            return water_counter


        height_scale = list(range(0, max(height)+1))
        height_scale.reverse()
        print(height_scale)
        for n in height_scale:
            switch = False
            hit_counter = 0
            for peak in height:
                if peak >= n:
                    print(f'n:{n} .......... Peak:{peak} .......... Pts:{hit_counter} .......... Total:{water_counter + hit_counter}')
                    print()
                    water_counter += hit_counter
                    hit_counter = 0
                    switch = True
                if (peak < n):
                    if switch:
                        hit_counter += 1

        return(water_counter)


launcher = Solution()
print(launcher.trap(height))