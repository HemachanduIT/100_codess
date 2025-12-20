import java.util.*;
public class max_repeated_word {
    public static void main(String...args){
        String arr[]={"hello","chandu","hello","srgec"};
        HashMap<String,Integer> res=new HashMap<>();
        for(String i:arr){
            if(res.containsKey(i)){
                res.put(i,res.get(i)+1);
            }else{
                res.put(i,1);

            }
        }
        // System.out.println(res);
        int maxx=Collections.max(res.values());
                // System.out.println(maxx);
        ArrayList<String> list=new ArrayList<>();
        for(HashMap.Entry<String,Integer> entry:res.entrySet()){
            if(entry.getValue()==maxx){
                list.add(entry.getKey());
            }

        }
        Collections.sort(list);
        System.out.println(list.get(0));

    }
}
