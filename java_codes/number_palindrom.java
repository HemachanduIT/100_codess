public class number_palindrom {
    public static void main(String...args){
        int n=121;
        int rev=0;
        int k=n;
        while(n>0){
            rev=rev*10+n%10;
            n/=10;
        }
        if(k==rev){
            System.out.println(k+" is a palindrome number");
        } else {
            System.out.println(k+" is not a palindrome number");
        }
        // System.out.println("rev is "+rev);
    }
}
