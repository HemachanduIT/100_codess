// package java_codess;
// import java.util.*;
public class Armstrongno {
    public static void main(String[]args){
        int n=153;
        int k=n;
        int s=0;
        int c=(int)Math.log10(n)+1;
        while(n>0){
            s=s+(int)Math.pow(n%10,c);
            n=n/10;
        }
        if(s==k){
            System.out.println(k+"is armstrong");
        }else{
            System.out.println(k+"is not armstrong");
        }
        
    }
}
//153 is armstrong no 1^3+5^3+3^3=153
