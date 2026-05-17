class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map=dict()
        for i in range(len(nums)):
            c=target-nums[i]
            if(c in hash_map):
                return [hash_map[c],i]
            hash_map[nums[i]]=i       
        
        