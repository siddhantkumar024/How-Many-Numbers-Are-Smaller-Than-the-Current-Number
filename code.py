class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums=sorted(nums)
        d={}
        for i , num in enumerate(snums):
            if num not in d:
                d[num]=i
        res=[]
        for num in nums:
            res.append(d[num])
        return res
        
