class Solution {
    public int[] findOriginalArray(int[] changed) {
        if(changed.length%2!=0) return new int[0];
        
        Queue<Integer> temp = new LinkedList<>();
        Arrays.sort(changed);
        
        for(int i=changed.length-1,k=changed.length-1; i>=0; i--){
            if(!temp.isEmpty() && temp.peek()==changed[i]*2) temp.poll();
            else{
                temp.add(changed[i]);
                changed[k]=changed[i]/2;
                k--;
            }
        }
      return (temp.isEmpty())? Arrays.copyOfRange(changed,changed.length/2,changed.length): new int[0];
    }
}