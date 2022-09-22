class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<>();
        for(String token : tokens){
            if("+-*/".contains(token)){
                int num2=st.pop(),num1=st.pop();
                switch(token.charAt(0)){
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
                st.push(Integer.parseInt(token));
            }            
        }
        
        return st.pop();
    }
}