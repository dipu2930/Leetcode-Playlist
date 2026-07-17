class Solution {
public:
    bool isPalindrome(int x) {
        int temp=x;
        double rev=0;
        int c;
        if(x<0){
         return 0;
        }
        while(x!=0){       
        c= x%10;
        rev=rev*10+c;
        x=x/10;
    }
    if(temp==rev){
        return true;
    }
    else{
        return false;
    }
    }
};