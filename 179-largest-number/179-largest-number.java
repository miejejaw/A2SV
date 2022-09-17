class Solution {
    public String largestNumber(int[] nums) {
       
        String[] temp = Arrays.stream(nums).mapToObj(String::valueOf).toArray(String[]::new);
        Arrays.sort(temp, new Comparator<String>(){
            public int compare(String a, String b) {
                return (b+a).compareTo(a+b);
            }
        } );
        
        return String.join("",temp).replaceFirst("^0+(?!$)", "");
    }
}