class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        last_smaller=float("-inf")
        largest=0
        count=0
        for i in range(0,n):
            num=nums[i]
            
            if num-1==last_smaller:
                count+=1
                last_smaller=num
            elif num!=last_smaller:
                count=1
                last_smaller=num
            largest=max(largest,count)
        return largest