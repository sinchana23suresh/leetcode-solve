// 15 ms | 12.6 MB
class Solution(object):
    def isAnagram(self, s, t):
        d = {}

        for char in s:
            d[char] = d.get(char, 0) + 1

        for char in t:
            d[char] = d.get(char, 0) - 1

        return all(value == 0 for value in d.values())

        
        