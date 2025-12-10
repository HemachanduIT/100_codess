public class string_palindrome {
    public static void main(String...args){
        String s="madam";
        String res="";
        StringBuilder sb=new StringBuilder(s);
        // StringBuffer str=new StringBuffer(s);
        res=sb.reverse().toString();
        if(s.equals(res)){
            System.out.println(s+" is a palindrome");
    }else{
        System.out.println(s+" is not a palindrome");
    }
}
}