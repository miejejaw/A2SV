class Solution {
    public int[] sortArray(int[] nums) {
        return sort(nums,0,nums.length-1);
    }
    public int[] sort(int[] nums ,int i , int j){
        if(j-i==0){
            int[] temp= {nums[i]};
            return temp;
        }
        int[] left= sort(nums,i,(i+j)/2);
        int[] right= sort(nums,(i+j)/2+1,j);
        return merge(left,right);
    }
    public int[] merge(int[] left, int[] right){
        int n =left.length+right.length;
        int[] temp = new int[n];
        for(int i=0,l=0,r=0; i<n; i++){
            if((r>=right.length && l<left.length) || (l<left.length && r<right.length && left[l]<right[r]))
                temp[i]=left[l++];
            else 
                temp[i]=right[r++];
        }
        return temp;
    }
}