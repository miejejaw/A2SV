class MinStack {
    Stack<Integer> st;
    int min= Integer.MAX_VALUE;
    public MinStack() {
        st= new Stack<>();
    }
    
    public void push(int val) {
        st.push(val);
        min = Math.min(min,val);
    }
    
    public void pop() {
       int val = st.pop(); 
       if(val==min){
           min= Integer.MAX_VALUE;
           for(int i=0; i<st.size(); i++){
             min = Math.min(min,st.get(i));  
           }
       }
    }
    
    public int top() {
        return st.peek();
    }
    
    public int getMin() {
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */