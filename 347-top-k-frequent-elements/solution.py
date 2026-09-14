// 13 ms | 15.1 MB
class Solution(object):
    def topKFrequent(self, nums, k):
        c={}
        for i in range(len(nums)):
            if nums[i] in c:
                c[nums[i]]=c[nums[i]]+1
            else:
                c[nums[i]]=1
        m=0
        for v in c.values():
            if v>m:
                m=v
        ans=[]
        for s in range(m,0,-1):
            for num in c:
                if c[num]==s:
                    ans.append(num)
                    if len(ans)==k:
                        return ans
                        "bucket sort is efficient method"
        