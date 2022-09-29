class Solution {
    public int[] shuffle(int[] nums, int n) {
        int arr[] = new int[nums.length];

        for(int i=0,j=n,k=1; i < n; i++, j++,k+=2){
            arr[k-1] = nums[i];
            arr[k] = nums[j];
        }
        return arr;   
    }
}