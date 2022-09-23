class Solution {
    public String reverseParentheses(String s) {
        
       Stack<Character> st = new Stack<>();
       for(int i=0; i<s.length(); i++){
           if(s.charAt(i)==')'){  
               Queue<Character> temp = new LinkedList<>();
               while(st.peek()!='('){
                   temp.add(st.pop());
               }
               st.pop();
               while(!temp.isEmpty()){
                   st.push(temp.poll());
               }
           }
           else{
               st.push(s.charAt(i));
           } 
       }
        
        String result="";
        while(!st.isEmpty()){
            result=st.pop()+result;
        }
        return result;
    }
}