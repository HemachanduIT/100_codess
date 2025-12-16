import java.util.*;
public class even_ids_count {
 public static void main(String...args){
    Scanner s=new Scanner(System.in);
    int n=s.nextInt();
    int count=0;
for(int i=0;i<n;i++){
    int x=s.nextInt();
    int digit=(int)Math.log10(x)+1;
    if(digit%2==0){
        count++;
    }
}
//  ArrayList<Integer> arr=new ArrayList<>();
// for(int i=0;i<n;i++){
//     arr.add(s.nextInt());
// }
// for(int x:arr){
//     String str=Integer.toString(x);
//     // int len=str.length();
//     if(str.length()%2==0){
// count+=1;
//     }
// }
System.out.println(count);
s.close();
 }    
}
