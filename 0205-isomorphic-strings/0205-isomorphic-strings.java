class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character,Character> temp = new HashMap<>();
        Map<Character,Character> temp2 = new HashMap<>();
        
        for(int i=0; i<s.length(); i++){
            if(temp.containsKey(s.charAt(i)) && t.charAt(i)!=temp.get(s.charAt(i)))
                return false;
            else if(temp.containsValue(t.charAt(i)) && temp2.get(t.charAt(i))!=s.charAt(i)){
                    return false;
            }
            temp.put(s.charAt(i),t.charAt(i));
            temp2.put(t.charAt(i),s.charAt(i));
        }
        return true;
    }
}