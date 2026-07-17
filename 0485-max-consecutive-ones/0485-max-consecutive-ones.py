class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_con = 0
        current_con = 0
        
        for num in nums:
            if num == 1:
                # Increment if we see a 1
                current_con += 1
            else:
                # If we see a 0, update our max and reset the current streak
                if current_con > max_con:
                    max_con = current_con
                current_con = 0
        if current_con>max_con:
            max_con=current_con        
        # Return the max in case the array ends with a streak of 1s
        return max_con