import java.util.*;
public class lcm{
    public static void main (String...args){
        Scanner s=new Scanner(System.in);
        int a=s.nextInt();int b=s.nextInt();
        int x=a;
        int y=b;
        while(a!=b){
            if(a>b){
                a-=b;
            }else{
                b-=a;
            }
        }
        // System.out.print("the gcd is",+a);
        System.out.println("the gcd is"+a);
        System.out.println("the lcm is"+(x*y)/a);
        
s.close();
    }
}