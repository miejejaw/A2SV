class MyHashSet {
    ArrayList<Integer>[] hold;
    public MyHashSet() {
        hold = new ArrayList[1001];
        for (int i = 0; i < 1001; i++) { 
            hold[i] = new ArrayList<Integer>(); 
        }
    }
    
    public void add(int key) {
        if(!hold[key%1000].contains(key)) hold[key%1000].add(key);
    }
    
    public void remove(int key) {
        if(hold[key%1000].contains(key)){
           hold[key%1000].remove(new Integer(key));
        }
    }
    
    public boolean contains(int key) {
        return hold[key%1000].contains(key);
    }
}
