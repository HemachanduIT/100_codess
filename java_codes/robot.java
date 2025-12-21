public class robot {
    public static void main(String...args){
        String input="G()(al)";
        char ch[]=input.toCharArray();
        String res="";
        // System.out.println(input);
        // System.out.println(ch[1]); 
        for(int i=0;i<ch.length;i++){
            if(ch[i]=='G'){
                res+="Go";
            }else if(ch[i]=='(' && ch[i+1]==')'){
                res+="Stop";
            }else if(ch[i]=='(' && ch[i+1]=='a' && ch[i+2]=='l' && ch[i+3]==')'){
                res+="Turn";
            }
        }
        System.out.println(res);
    }
}
