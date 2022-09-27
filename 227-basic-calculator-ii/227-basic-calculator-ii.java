import java.util.StringTokenizer;
class Solution {
    public int calculate(String s) {
        Deque<String> nums = new ArrayDeque<>();       
        ArrayList<String> temp = new ArrayList<>();  
        s= s.replaceAll(" ","");
        StringTokenizer str =  new StringTokenizer(s, "+ - * /",true);
        while(str.hasMoreTokens()){
			temp.add(str.nextToken());
		}
        
        for(int i=0; i<temp.size(); i++){
           if(temp.get(i).equals("*") || temp.get(i).equals("/")){
               int num1= Integer.parseInt(nums.pollLast());
               int num2= Integer.parseInt(temp.get(i+1));
               int result;
               if(temp.get(i).equals("*")) result=num1*num2;
               else result=num1/num2;
               nums.add(String.valueOf(result));
               i++;
           }
           else{
                nums.add(temp.get(i));
           }
        }
        
        int result=Integer.valueOf(nums.pollFirst());
        while(!nums.isEmpty()){
               String op = nums.pollFirst();
               int num= Integer.valueOf(nums.pollFirst());
               if(op.charAt(0)=='+') result+=num;
               else result-=num;
        }
    
        
        return result;
    }
}

