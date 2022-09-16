class Solution {
    public int[][] merge(int[][] interval) {
        Arrays.sort(interval,Comparator.comparingInt(v->v[0]));
        int k=0,x=interval[0][0],y=interval[0][1];
           
        for(int i=1; i<interval.length;){
            if(interval[i][0]>y){
                interval[k][0] = x;
                interval[k][1] = y; 
                k++;
                x=interval[i][0];
                y=interval[i][1];
            }
            else {
                if(interval[i][1]>y)
                    y = interval[i][1];
                i++;                
            }
            
        }
        interval[k][0] = x;
        interval[k][1] = y; 
        
        return Arrays.copyOf(interval,k+1);
    }
}