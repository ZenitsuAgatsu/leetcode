class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map={}
        res=[]
        for i in range(len(nums1)):
            hash_map[nums1[i]]=hash_map.get(nums1[i],0)+1

        for j in nums2:
            if j in hash_map:
                res.append(j)
        return list(set(res))                    