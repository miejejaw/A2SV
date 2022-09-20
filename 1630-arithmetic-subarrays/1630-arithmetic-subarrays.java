class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> result = new ArrayList<>();
        
        for(int i=0; i<l.length; i++){
            int[] temp = Arrays.copyOfRange(nums,l[i],r[i]+1);
            
            if(temp.length<3) {
                result.add(true); 
                continue;
            }
            Arrays.sort(temp);
            int gap = temp[1]-temp[0];
            for(int j=2; j<temp.length; j++){
                if(temp[j]-temp[j-1]!=gap) {
                    result.add(false); 
                    break;
                }
            }
            if(result.size()==i) result.add(true);
        }
        return result;
    }
}