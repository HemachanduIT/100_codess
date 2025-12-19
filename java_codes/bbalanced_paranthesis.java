public class bbalanced_paranthesis {
    public static void main(String...args){
        // String s=")))()(((";
        String s="(())";

        char ch[]=s.toCharArray();
        int c=0;
        int f=0;
        // System.out.println(ch[0]);
        for(char i:ch){
            if(i=='('){
                c+=1;
            }else if(i==')'){
                c-=1;
            }
            if(c<0){
                f=1;
                            System.out.println(s+" is NOT  AN valid paranathesis");

                break;
            }

        }
        if(f!=1){
        if(c==0){
            System.out.println(s+" is an valid paranathesis");
        }else{
            System.out.println(s+" is NOT  AN valid paranathesis");

        }
    }
    }
}
