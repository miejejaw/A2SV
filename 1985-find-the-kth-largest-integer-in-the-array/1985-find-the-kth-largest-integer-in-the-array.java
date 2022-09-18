class Solution {
    public String kthLargestNumber(String[] nums, int k) {
       Arrays.sort(nums,new Comparator<String>(){
           public int compare(String a , String b){
               if(a.length() != b.length()) return b.length() - a.length();
               return (b+a).compareTo(a+b);
           }
       });
        System.out.print(Arrays.toString(nums));
       return nums[k-1];
    }
}