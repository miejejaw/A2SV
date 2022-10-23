class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> temp = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(temp.containsKey(target-nums[i])){
                int[] ans = {temp.get(target-nums[i]) , i};
                return ans;
            }
            temp.put(nums[i],i);
        }
        return new int[0];
    }
}