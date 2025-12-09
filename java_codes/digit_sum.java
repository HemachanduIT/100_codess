public class digit_sum {
    public static void main(String...args){

    
    int n=123;
    int s=0;
    while(n>0){
        s=s+n%10;
        n=n/10;
    }
    System.out.println(s);
}
}
