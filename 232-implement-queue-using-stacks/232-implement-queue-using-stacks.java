class MyQueue {
   Stack<Integer> stack;
    public MyQueue() {
        stack = new Stack<>();
    }
    
    public void push(int x) {
        stack.push(x);
    }
    
    public int pop() {
       int temp= stack.get(0);
       stack.removeElementAt(0);
       return temp;
    }
    
    public int peek() {
       return stack.get(0);
    }
    
    public boolean empty() {
        return stack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */