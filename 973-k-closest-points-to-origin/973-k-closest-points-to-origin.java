class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {  
                int x= (int)(Math.pow(a[0],2) + Math.pow(a[1],2));
                int y= (int)(Math.pow(b[0],2) + Math.pow(b[1],2));
                return x-y;
            }
        });        
        
        return Arrays.copyOf(points, k);
    }
}

        // Arrays.sort(points, Comparator.comparingInt(v -> v[0] * v[0] + v[1] * v[1]));        
