class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        s=0
        p=1
        while temp>0:
            r=temp%10
            p*=r
            s+=r
            temp//=10
        return (p-s)
        