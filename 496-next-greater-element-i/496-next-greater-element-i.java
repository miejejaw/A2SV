class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> st = new Stack<>();
        HashMap<Integer,Integer> result = new HashMap<>();
        
        for(int i=0; i<nums2.length; i++){
            result.put(nums2[i],-1);
            while(!st.isEmpty() && nums2[i]>st.peek()){
                result.replace(st.pop(),nums2[i]);
            }
            st.push(nums2[i]);
        }
        
        
        for(int i=0; i<nums1.length; i++){
             nums1[i]=result.get(nums1[i]);
         }
        return nums1;
    }
}