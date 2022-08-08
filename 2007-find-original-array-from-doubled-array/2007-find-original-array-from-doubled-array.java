class Solution {
    public int[] findOriginalArray(int[] changed) {
        if(changed.length%2!=0) return new int[0];
        int[] result = new int[changed.length/2];
        Arrays.sort(changed);
        Queue<Integer> temp = new LinkedList<>();
        
        for(int i=0,k=0; i<changed.length; i++){

            if(!temp.isEmpty() && temp.peek()==changed[i]){
                temp.poll();
            }
            else if(!temp.isEmpty() && temp.peek()<changed[i] || k>=result.length){
                return new int[0];
            }
            else {
                result[k]=changed[i];
                temp.add(changed[i]*2);
                k++;
            }
        }
 
        return result;
    }
}