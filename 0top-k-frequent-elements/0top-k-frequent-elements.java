class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        PriorityQueue<Pair<Integer, Integer> > temp = new PriorityQueue<>((a, b) -> b.getValue()-a.getValue());      
        Map<Integer,Integer> freq = new HashMap<>();
        int[] result = new int[k];
        for(int num: nums){
            freq.put(num,freq.getOrDefault(num, 0)+1);
        }

         for(Map.Entry m : freq.entrySet()){  
            temp.add(new Pair<>((int)m.getKey(),(int)m.getValue()));
         }
         for(int i=0; i<result.length; i++){
             result[i]=temp.poll().getKey();
         }
        return result;
    }
}