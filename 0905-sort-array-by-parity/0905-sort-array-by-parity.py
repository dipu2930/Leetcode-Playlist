class Solution:
    def func(self, nums, l, r):
        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1
        
        return nums

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return self.func(nums, 0, len(nums) - 1)