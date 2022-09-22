class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> st = new Stack<>();
        for(int i=0; i<s.length(); i++){
            switch(s.charAt(i)){
                case '(':
                    st.push(')');
                    break;
                case '{':
                    st.push('}');
                    break;
                case '[':
                    st.push(']');
                    break;
                default:
                    if(!st.isEmpty() && st.peek()== s.charAt(i))
                        st.pop();
                    else
                        return false;
            }
        }
        return (st.isEmpty())? true: false;
    }
}