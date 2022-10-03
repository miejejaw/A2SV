class Solution {
    HashMap<Integer,Integer> cache = new HashMap<>();
    public int climbStairs(int n) {
        if(cache.containsKey(n)) return cache.get(n);
        int result;
        if(n<4) result = n;
        else result = climbStairs(n-1)+climbStairs(n-2);
        
        cache.put(n,result);
        return result;
    }
}