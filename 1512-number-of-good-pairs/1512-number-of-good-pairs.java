class Solution {
    public int numIdenticalPairs(int[] nums) {
        Arrays.sort(nums);
        int count=0,temp=0;
        for(int i=1,j=0; i<nums.length; i++){
            if(nums[i]==nums[j]) {
                temp++;
            }
            else{
                count+=factorial(temp);
                temp=0;
                j=i;
            }
        }
        count+=factorial(temp);
        return count;
    }
    public static int factorial(int number) {
        int result = 0;

        for (int i = 1; i <= number; i++) {
            result += i;
        }

        return result;
    }
}

