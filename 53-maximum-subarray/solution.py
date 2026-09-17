// 41 ms | 21.1 MB
class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        final = nums[0]

        for i in range(1, len(nums)):
            if current + nums[i] < nums[i]:
                current = nums[i]
            else:
                current = current + nums[i]

            if current > final:
                final = current

        return final