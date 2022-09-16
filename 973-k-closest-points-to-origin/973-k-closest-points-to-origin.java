class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {  
                int x= (int)(Math.pow(a[0],2) + Math.pow(a[1],2));
                int y= (int)(Math.pow(b[0],2) + Math.pow(b[1],2));
                return x-y;
            }
        });
        
        int[][] result = new int[k][2];
        for(int i=0; i<k; i++){
            result[i][0] = points[i][0];
            result[i][1] = points[i][1];
        }
        
        return result;
    }
}