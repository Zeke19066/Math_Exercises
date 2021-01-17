
"""
:type lists: List[ListNode]
:rtype: ListNode
"""

lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

class Solution(object):
    def mergeKLists(self, lists):
        flat_list = []
        for sub_list in lists:
            for item in sub_list:
                flat_list.append(item)
        flat_list.sort()
        print(flat_list)


run = Solution()
run.mergeKLists(lists)