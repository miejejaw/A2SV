class MyHashSet {
	boolean[] flag;
    public MyHashSet() {
		flag = new boolean[1000001];
	}
    
    public void add(int key) {
        flag[key]=true;
    }
    
    public void remove(int key) {
        flag[key]=false;
    }
    
    public boolean contains(int key) {
        return flag[key];
    }
}

