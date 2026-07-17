class Solution {
    public void sortColors(int[] nums) {
        int red=0;
        int white=1;
        int blue=2;
        int t;
        int n=nums.length;
        int res[]= new int[n];
     for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
      if(nums[i]>nums[j]){
        t=nums[i];
        nums[i]=nums[j];
        nums[j]=t;
      }
     }
     }
     System.out.println(nums);   
    }
}