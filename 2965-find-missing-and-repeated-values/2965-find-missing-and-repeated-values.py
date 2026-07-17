class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        s= set()
        n= len(grid)
        a=0
        b=0
        expSum=0
        actualSum=0
        for i in range(n):
            for j in range(n):
                val= grid[i][j]
                actualSum+=val
                if val in s:
                    a=val
                    ans.append(a)
                s.add(val)
        expSum = (n*n)*(n*n +1)//2
        b= expSum +a - actualSum
        ans.append(b)
        return ans
        