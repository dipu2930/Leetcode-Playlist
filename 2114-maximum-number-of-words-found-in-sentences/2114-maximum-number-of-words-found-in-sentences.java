class Solution {
    public int mostWordsFound(String[] sentences) {
        int n=sentences.length;
        int count=0;
        int Max_count=-1;
        for(int i=0;i<sentences.length;i++){
            count =1;
            for(int j=0; j<sentences[i].length();j++){
                if(sentences[i].charAt(j)==' '){
                    count+=1;
                }
            }
            if(count>Max_count){
                Max_count=count;
            }
        }
        return Max_count;
        
        
    }
}