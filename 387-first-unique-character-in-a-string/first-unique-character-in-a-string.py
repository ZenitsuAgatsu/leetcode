class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        for i in d:
            if d[i]==1:
                return s.find(i)
                break
        return -1        
            
                 
                  