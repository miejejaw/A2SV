class Solution {
    public String removeKdigits(String num, int k) {
        char[] arr = num.toCharArray();
        int index = -1 ;
        for(int i = 0 ; i < arr.length ; i++) {
            while(k > 0 && index >= 0 && arr[i] < arr[index] ) {
                index-- ;
                k-- ;
            }
            if (index != -1 || arr[i] != '0') arr[++index] = arr[i];
        }
        
        if (index+1 <= k ) return "0";
        return String.valueOf(arr, 0, index+1-k);
    }
}