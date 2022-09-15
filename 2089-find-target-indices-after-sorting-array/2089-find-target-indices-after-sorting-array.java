class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> result = new ArrayList<>();
        Arrays.sort(nums);
        for(int i=0; i<nums.length; i++){
            if(target== nums[i]) result.add(i);
            else if(target<nums[i]) break;
        }
        return result;
    }
}