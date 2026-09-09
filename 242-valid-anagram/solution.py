// 21 ms | 14.7 MB
class Solution(object):
    def isAnagram(self, s, t):
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]]=d1[s[i]]+1
            else:
                d1[s[i]]=1

        for i in range(len(t)):
            if t[i] in d2:
                d2[t[i]]=d2[t[i]]+1
            else:
                d2[t[i]]=1

        if d1==d2:
            return True
        else:
            return False
        
        