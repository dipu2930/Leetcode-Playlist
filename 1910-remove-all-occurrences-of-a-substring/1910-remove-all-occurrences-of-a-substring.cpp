class Solution {
public:
    string removeOccurrences(string s, string part) {
        int p;
        while(true){
           p=s.find(part);
           if(p==-1){
            break;
           } 
           s.erase(p,part.length());
           
        }
        return s;
        
    }
};