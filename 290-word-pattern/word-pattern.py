class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x=s.split()
        if(len(pattern)!=len(x)):
            return False
        d={}
        d2={}
        for ch in range(len(pattern)):
            a=pattern[ch]
            b=x[ch]
            if a in d:
                if d[a]!=b:
                    return False
            else:
                d[a]=b

            if b in d2:
                if(d2[b]!=a):
                    return False
            else:
                d2[b]=a
        return True                            

        