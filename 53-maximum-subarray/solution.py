// 104 ms | 21.3 MB
class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        final = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            final = max(final, current)

        return final