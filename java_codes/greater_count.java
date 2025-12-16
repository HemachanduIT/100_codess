import java.util.*;
public class greater_count{
    public static void main(String...args){
Scanner s =new Scanner(System.in);
int n=s.nextInt();
int arr[]=new int[n];
ArrayList<Integer> res=new ArrayList<>();
for(int i=0;i<n;i++){
arr[i]=s.nextInt();
// arr.add(s.nextInt());
}
for(int i=0;i<n;i++){
int c=0;
int maxx=arr[i];
for(int j=0;j<n;j++){
    if(maxx>arr[j]){
        c+=1;
    }
}
res.add(c);
}
System.out.println(" "+res);

s.close();
    }
}