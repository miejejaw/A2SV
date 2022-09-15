class Solution {
    public void sortColors(int[] nums) {
        
        int[] colors = new int[3];
        for(int i:nums) colors[i]++;
        for(int i=0,c=0; i<nums.length; i++){
            while(colors[c]==0){
                c++;
            }
            nums[i]=c;
            colors[c]--;
        }
    }
}