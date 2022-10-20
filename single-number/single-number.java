class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i: nums){
            if(set.contains(i))
                set.remove(i);
            else 
                set.add(i);
        }
        for (Integer i : set) {
            return i;
        }
        return 0;
    }
}