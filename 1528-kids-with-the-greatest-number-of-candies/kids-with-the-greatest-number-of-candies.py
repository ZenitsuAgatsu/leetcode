class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       maxcandy=max(candies)
       result=[]
       for i in candies:
        result.append((i+extraCandies)>= maxcandy)

       return result   



