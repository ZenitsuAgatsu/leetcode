class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1

        for j in range(0,k):
            x=max(d,key=d.get)
            res.append(x)
            d.pop(x)
        return res    
                
        