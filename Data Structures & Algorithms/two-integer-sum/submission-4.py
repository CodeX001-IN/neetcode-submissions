class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1,i in enumerate (nums):
            j=target-i
            if j in nums:
                index2= nums.index(j)
                if index1!=index2 :
                    return sorted([index1,index2])