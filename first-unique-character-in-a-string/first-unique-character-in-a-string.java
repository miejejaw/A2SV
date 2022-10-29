class Solution {
    public int firstUniqChar(String s) {
        Map<Character,Integer> temp = new LinkedHashMap<>();
        for(int i=0; i<s.length(); i++){
            char x = s.charAt(i);
            temp.put(x,temp.getOrDefault(x,0)+1);
        }
        char ans=' ';
        for(char i : temp.keySet()) {
            if(temp.get(i)==1){  ans=i; break; }            
        }
        return s.indexOf(ans);
    }
}