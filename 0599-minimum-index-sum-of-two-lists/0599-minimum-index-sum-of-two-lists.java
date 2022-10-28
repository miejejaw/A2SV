class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String,Integer> temp = new HashMap<>();
        Stack<String> st = new Stack<>();
        int min = Integer.MAX_VALUE;
        
        for(int i=0; i<list1.length; i++){
            temp.put(list1[i],i);
        }
        for(int i=0; i<list2.length; i++){
            if(temp.containsKey(list2[i])){
                int x =i+temp.get(list2[i]);
                if(!st.isEmpty() && temp.get(st.peek())==x){
                   st.push(list2[i]);
                }
                else if(!st.isEmpty() && temp.get(st.peek())>x){
                    st.clear();
                    st.push(list2[i]);
                }
                else if(st.isEmpty())
                    st.push(list2[i]);
                temp.put(list2[i],x); 
            }

        }
        String[] ans = new String[st.size()];
        int k=0;
        while(!st.isEmpty()){
            ans[k++]=st.pop();
        }
        return ans;
    }
}