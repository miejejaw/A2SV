class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, Comparator.comparingInt(v -> v[0] * v[0] + v[1] * v[1]));        
        
        return Arrays.copyOf(points, k);
    }
}