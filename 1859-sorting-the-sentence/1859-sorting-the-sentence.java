class Solution {
    public String sortSentence(String s) {
      String result = "";
      int i=1;
      s=" "+s;
      while(s.indexOf(String.valueOf(i))!=-1){
          int j=s.indexOf(String.valueOf(i));
          int k=j-2;
          while(s.charAt(k)!=' '){
              k--;
          }
          result += s.substring(k,j);
          // s=s.replace()
          i++;
      }
     return result.trim();
    }
}