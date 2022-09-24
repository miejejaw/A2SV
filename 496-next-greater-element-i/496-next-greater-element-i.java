class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
      Stack<Integer> ss = new Stack<>();
      Map<Integer,Integer> arr = new HashMap<>(); 

        for(int num: nums2){           
            while(!ss.isEmpty() && num>ss.peek()){
                arr.put(ss.pop(),num);                
            }
            ss.add(num);                
        }   
        for(int i=0; i<nums1.length; i++){
             nums1[i] =arr.getOrDefault(nums1[i],-1);                           
        }
      
        return nums1;
    }
}