class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        if(x<0):
            return False
        else:
            rev=0
            r=len(str(x))-1
            for i in range(len(str(x))):
                rev=rev+((x%10)*(10**r))
                x=int(x/10)
                r-=1
            if(y==rev):
                return True
            else:
                return False        
