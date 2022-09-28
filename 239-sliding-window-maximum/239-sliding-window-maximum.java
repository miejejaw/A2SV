class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dec = new ArrayDeque<>();
        int[] result = new int[nums.length-k+1];
        k-=2;
        for(int i=0,j=0; i<nums.length; i++){
            while(!dec.isEmpty() && nums[i]>dec.peekLast()){
                dec.pollLast();
            }
            dec.add(nums[i]);
           
            if(i>k){
                result[j]=dec.peek();
                if(dec.peek()==nums[j]) dec.poll();
                j++;
            }
            
        }
        return result;
    }
}