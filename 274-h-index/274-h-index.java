class Solution {
    public int hIndex(int[] citations) {
          
      Arrays.sort(citations);
      if(citations[citations.length-1]==0) return 0;
      if(citations.length==1) return 1;
      int h=0,l=0,r=citations.length,mid;
      while(r>=l){
            mid=(r+l)/2;
            if(citations[mid]>=citations.length-mid){ h=citations.length-mid; r=mid-1; }
            else l=mid+1;
      }
        return h;
    }
}