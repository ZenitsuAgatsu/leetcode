class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0

        for n in s:
            count=0
            current=n
            if n-1 not in s:
                count=0
                current=n
                while current in s:
                    count+=1
                    current+=1
                longest=max(longest,count)
        return longest        



            




            



        