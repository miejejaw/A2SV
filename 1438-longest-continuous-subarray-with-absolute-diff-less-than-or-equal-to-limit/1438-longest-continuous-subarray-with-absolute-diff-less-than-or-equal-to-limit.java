class Solution {
    public int longestSubarray(int[] nums, int limit) {

        Deque<Integer> in = new LinkedList<>();
        Deque<Integer> de = new LinkedList<>();
        int max=0; 

        for(int i=0,j=0; i<nums.length; i++){
              
            while(!in.isEmpty() && nums[i]>in.peekLast()){
                in.pollLast();
            }in.addLast(nums[i]);
            
            while(!de.isEmpty() && nums[i]<de.peekLast()){
                de.pollLast();
            }de.addLast(nums[i]);

            while((!de.isEmpty()&&!in.isEmpty()) && in.peek()-de.peek()>limit){                 
              if(de.peek()==nums[j]) de.poll(); 
              if(in.peek()==nums[j]) in.poll();              
              j++;
            }
            max=Math.max(max, i-j);              
        }
        return max+1;
    }
} 
