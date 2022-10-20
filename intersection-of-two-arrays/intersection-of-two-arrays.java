class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        for(int i: nums1){
            set.add(i);
        }
        int j=0;
        for(int i: nums2){
            if(set.contains(i)){
                set.remove(i);
                nums2[j++]= i;
            }           
        }
        return Arrays.copyOf(nums2,j);
    }
}