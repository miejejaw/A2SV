class Solution{
    public int lengthOfLongestSubstring(String s) {
        
        Map<Character, Integer> map = new HashMap<>();
        int max=0;
		
        for(int i=0, j=-1; i<s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch) && map.get(ch) >= j)
                j = map.get(ch);
            max = Math.max(i-j, max);
            map.put(ch, i);            
        }
        return max;
    
    }
}