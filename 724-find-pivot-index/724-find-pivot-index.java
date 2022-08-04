class Solution {
    public int pivotIndex(int[] nums) {
        int piv=1,rsum=0,lsum=0;
        for(int k=1; k<nums.length; k++){
            rsum+=nums[k];
        }
        if(rsum==0) return 0;
        
        while(piv<nums.length){               
            lsum+=nums[piv-1];
            rsum-=nums[piv];
            if(rsum==lsum) return piv;
            piv++;
        }
        return -1;
    }
}