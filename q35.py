class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        t = len(nums)
        nums.append(int(target))
        nums.sort()
        x = nums.index(target)
        return x
