class Solution {
    public int maxArea(int[] height) {
        
        int max=0,l=0,r=height.length-1;
        while(r>l){
            
           max=Math.max(max,(r-l)*Math.min(height[l],height[r]));
           if(height[l] > height[r]) r--;           
           else if(height[l] < height[r]) l++;
           else {l++; r--;}
        }
        
        return max;
    }
}