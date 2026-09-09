// 24 ms | 13.4 MB
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

        
        