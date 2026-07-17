class Solution {
    public int lengthOfLastWord(String s) {
        s=s.trim();
        // String[] words=s.split("\\s+");
        // String result = "";
        // // for(int i=0;i<words.length;i++){
        // //     result += words[i];
        // // }
        // int n= words.length;
        // for(int i=0;i<n;i++){
        //   result+= words[i];
        // }
        // return result.length();
        int j=s.length()-1;
        int i;
        if(s.length() == 1) return 1;
        for(i=s.length()-1;i>=0;i--){
            if(s.charAt(i) == ' '){
                return j-i;
            }
        }
        return j-i;
        
    }
}