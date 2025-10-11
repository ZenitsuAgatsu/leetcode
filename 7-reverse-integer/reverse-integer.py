class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            y=-x
        else:
            y=x    
        n=len(str(y))
        r=n-1
        out=0
        for i in range(n):
            p=y%(10)
            out=out+(p*(10**r))
            y=int(y/(10))
            r=r-1    

        if(x<0):
            z=-out
        else:
            z=out

        if(z<-2**31 or z>(2**31)-1):
            return 0
        else:
            return z            
            

