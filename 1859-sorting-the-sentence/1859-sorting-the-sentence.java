class Solution {
    public String sortSentence(String s) {
      String result = "";
      int i=1;
      while(s.indexOf(String.valueOf(i))!=-1){
          int j=s.indexOf(String.valueOf(i));
          int k=j-2;
          while(k>=0 && s.charAt(k)!=' '){
              k--;
          }
          result += s.substring(k+1,j)+" ";
          i++;
      }
     return result.trim();
    }
}