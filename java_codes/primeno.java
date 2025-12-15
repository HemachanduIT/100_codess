public class primeno {
    public static void main(String...args){
        int n=12;
        int c=0;
        for(int i=1;i<=n;i++){
            if(n%i==0)
                c+=1;
        }
        if(c==2){
            System.out.println(n+"is a prime no");

        }else{
            System.out.println(n+"is not a prime no");
        }
    }    
}
