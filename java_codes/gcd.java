import java.util.*;
public class gcd{
    public static void main (String...args){
        Scanner s=new Scanner(System.in);
        int a=s.nextInt();int b=s.nextInt();
        while(a!=b){
            if(a>b){
                a-=b;
            }else{
                b-=a;
            }
        }
        // System.out.print("the gcd is",+a);
        System.out.println("the gcd is"+a);
s.close();
    }
}