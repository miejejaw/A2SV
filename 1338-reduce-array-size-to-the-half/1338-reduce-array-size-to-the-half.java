class Solution {
    public int minSetSize(int[] arr) {
        Arrays.sort(arr);
        int sum=0,min=Integer.MAX_VALUE,k=0,temp=arr[0],count=1;
        for(int i=1; i<arr.length; i++){
            if(arr[i]!=temp){
              arr[k++]=count;
              count=0;
              temp=arr[i];
            }
            count++;
        }
        if(count>1) arr[k++]=count;

        Arrays.sort(arr,0,k);
        for(int i=0,j=0; i<=k; ){
            if(sum>=arr.length/2){
                min = Math.min(min,i-j);
                sum-=arr[j++];
            } 
            else{
                sum+=arr[i++];
            }                       
        }
        return min;
    }
}