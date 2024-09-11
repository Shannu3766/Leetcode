class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ks=0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if((nums[i]+nums[j])==target and i!=j):
                    k=[i,j]
                    ks=1
                    break
            if(ks==1):
                break
        return k