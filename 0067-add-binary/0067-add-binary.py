class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i=len(a)-1
        j=len(b)-1
        l3=[]
        
        carry=0
        while i>=0 or j>=0 or carry==1:
            
            if i>=0:
                carry=carry+int(a[i])
                i-=1
            if j>=0:
                carry=carry+int(b[j])
                j-=1
            l3.append(str(carry%2))
            carry=carry//2
        l3.reverse()
        result=''.join(l3)
        return result

        