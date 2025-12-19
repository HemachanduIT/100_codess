import java.util.*;
public class word_counter {
    public static void      main(String...args){
        Scanner s =new Scanner(System.in);
        int n=s.nextInt();
        String arr[]=new String[n];
        for(int i=0;i<n;i++)
            arr[i]=s.next();
        HashMap<String,Integer> res=new HashMap<>();
        for(String i:arr){
            if(res.containsKey(i)){
                res.put(i,res.get(i)+1);
            }else{
                res.put(i,1);
            }
        }
        System.out.println(res);
        s.close();
    }
        }

