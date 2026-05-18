class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        d2={}
        x=ransomNote
        y=magazine

        for i in range(len(x)):
            d[x[i]]=d.get(x[i],0)+1

        for j in range(len(y)):
            d2[y[j]]=d2.get(y[j],0)+1    

        for ch in x:
            if ch in d2:
                if d2[ch]<d[ch]:
                    return False   
            else:
                return False  
        return True           
        