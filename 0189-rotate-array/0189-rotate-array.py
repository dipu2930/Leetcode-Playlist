class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k: ]+nums[ :n-k]
        # rot=k%n
        # for _ in range(0,rot):
        #     e=nums.pop()
        #     nums.insert(0,e)
        """
        Do not return anything, modify nums in-place instead.
        """
        