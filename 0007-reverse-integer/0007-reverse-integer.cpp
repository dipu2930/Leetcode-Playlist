class Solution {
public:
    int reverse(int x) {
        double rev=0;
        int c;
        while(x!=0){
            c=x%10;
             rev=rev*10+c;
            x=x/10;   
    }
    if(rev<INT_MIN || rev>INT_MAX){
             return 0;
        }   
    return rev;
 }
    
};