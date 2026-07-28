class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        max=(nums[n-1]-1)*(nums[n-2]-1)
        return max
        