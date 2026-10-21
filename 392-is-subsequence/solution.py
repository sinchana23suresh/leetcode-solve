// 0 ms | 11.9 MB
class Solution(object):
    def isSubsequence(self, s, t):
        l=len(s)
        index=0
        while index<l:
                i=t.find(s[index])
                if i==-1:
                    return False
                else:
                    t=t[i+1:]
                    index=index+1
        return True
        

        
        

        