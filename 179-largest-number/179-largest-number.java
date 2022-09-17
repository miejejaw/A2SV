class Solution {
    public String largestNumber(int[] nums) {
       
        Integer[] data =  Arrays.stream(nums).boxed().toArray( Integer[]::new );
        Arrays.sort(data, new Comparator<Integer>(){
            public int compare(Integer a, Integer b) {
                return (String.valueOf(b) + String.valueOf(a)).compareTo(String.valueOf(a) + String.valueOf(b));
            }
        });
        
        return Arrays.toString(data).replaceAll("\\[|\\]|,|\\s", "").replaceFirst("^0+(?!$)", "");
    }
}