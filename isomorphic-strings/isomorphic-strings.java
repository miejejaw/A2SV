import java.util.Map.Entry;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character,Character> temp = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            if(temp.containsKey(s.charAt(i)) && t.charAt(i)!=temp.get(s.charAt(i)))
                return false;
            else if(temp.containsValue(t.charAt(i))){
                for(Entry<Character,Character> entry: temp.entrySet()) {
                  if(entry.getValue() == t.charAt(i) && entry.getKey()!=s.charAt(i)) {
                    return false;
                  }
                }
            }
            temp.put(s.charAt(i),t.charAt(i));
        }
        return true;
    }
}