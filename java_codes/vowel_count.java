// import java.util.*;
public class vowel_count{
    public static void main(String...args){
        String s="Hema chandu";
        int vc=0,cc=0;
        // char arr[]={'a','e','i','o','u','A','E','I','O','U'};
        String vowels="aeiouAEIOU";
        char check[]=s.toCharArray();
        for(char i:check){
            if(vowels.indexOf(i)!=-1){
                vc+=1;
            }else{
                cc+=1;

            }
            }
        
        System.out.println("the vowel count is"+vc);
        System.out.println("the consonant count is"+cc);
        }
}