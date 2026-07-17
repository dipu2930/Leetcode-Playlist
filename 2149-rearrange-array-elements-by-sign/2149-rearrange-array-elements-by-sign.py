class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # pos=[]
        # neg=[]
        
        # for i in range(0,n):
        #     if nums[i]>0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # p=len(pos)
        # for j in range(0,p):
        #         nums[2*j]=pos[j]
        #         nums[2*j+1]=neg[j]
        pos_idx=0
        neg_idx=1
        res=[0]*n
        for i in range(0,n):
            if nums[i]>0:
                res[pos_idx]=nums[i]
                pos_idx+=2
            else:
                res[neg_idx]=nums[i]
                neg_idx+=2
        return res
        
        