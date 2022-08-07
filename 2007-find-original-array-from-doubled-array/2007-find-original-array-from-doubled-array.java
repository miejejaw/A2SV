class Solution {
    public int[] findOriginalArray(int[] changed) {
        if(changed.length%2!=0) return new int[0];
        int[] result = new int[changed.length/2];

        ArrayList<Integer> temp = IntStream.of(changed).boxed().collect(Collectors.toCollection(ArrayList::new));
        Collections.sort(temp, Collections.reverseOrder());
        
        for(int i=1,j=0; i<temp.size();){
            if(temp.get(i)*2==temp.get(j)) {
                result[j]= temp.remove(i);
                 
                if(result[j]==0) i++;
                j++;
            }
            else i++;  
        }
        System.out.print(temp);
        return (temp.size()==result.length)?result:new int[0];
    }
}