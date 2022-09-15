class Solution {
    public void sortColors(int[] nums) {
        int start=0,end=nums.length-1;
        for(int i=0; i<=end; i++){
            if(nums[i]==0) {
                swap(nums,i,start);
                start++;                 
            }
            else if(nums[i]==2) {
                swap(nums,i,end);
                end--;
                i--;
            }
        }
    }
    public static void swap(int [] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}