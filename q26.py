class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for i in range(i+1,len(nums)-1):
            j=i+1

            for j in range(j+1,len(len(nums))):
                if nums[i] == nums[j]:
                    del nums[j]
        len_list = nums
        return(len_list, nums)q26.p
