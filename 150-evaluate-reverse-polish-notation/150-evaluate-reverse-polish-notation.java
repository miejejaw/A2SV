class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<>();
        for(int i=0; i<tokens.length; i++){
            if((int)tokens[i].charAt(0)<48 && tokens[i].length()==1){
                int num2=st.pop();
                int num1=st.pop();
                switch(tokens[i].charAt(0)){
                    case '+':
                        st.push(num1+num2);
                        break;
                    case '-':
                        st.push(num1-num2);
                        break;
                    case '*':
                        st.push(num1*num2);
                        break;
                    case '/':
                        st.push(num1/num2);
                }
            }
            else{
                st.push(Integer.valueOf(tokens[i]));
            }            
        }
        
        return st.pop();
    }
}