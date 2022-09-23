class Solution {
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Integer> freq = new PriorityQueue(Collections.reverseOrder());
        Map<Character,Integer> counts = new HashMap();
       
        for(char ch:tasks){
            counts.put(ch,counts.getOrDefault(ch,0)+1);
        }
        freq.addAll(counts.values());
       
        int count=0;       
        while(!freq.isEmpty()){
            ArrayList<Integer> temp = new ArrayList<>();
            for(int i=0; i<=n; i++){
                if(!freq.isEmpty()) {
                    int tmp = freq.remove()-1;
                    if(tmp>0) temp.add(tmp);
                }
                else if(temp.isEmpty()) return count;
                count++;
            }        
            freq.addAll(temp);
        }
        return count;
    }
}