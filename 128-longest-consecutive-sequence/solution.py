// 53 ms | 26.9 MB
class Solution(object):
    def longestConsecutive(self, nums):
        seen=set(nums)
        longest=0
        for num in seen:
            if num-1 not in seen:
                current=num
                count=1
                while current+1 in seen:
                    current=current+1
                    count=count+1
                longest=max(count,longest)
        return longest

            
        