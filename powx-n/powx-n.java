class Solution {
    public double myPow(double x, int n) { 
        double result = power(x,Math.abs(n));
        return (n>0)? result: 1/result;

    }
    
    public double power(double x, int n){
         if(n==0) return 1;
         return (n%2==0)? power(x*x, n/2) : x*power(x*x, n/2);
    }
}