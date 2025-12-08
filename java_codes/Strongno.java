public class Strongno {
    public static void main(String[]args){
        // Scanner s=new Scanner(System.in);
        int n=148;
        int k=n;
        int sum=0,f=1;
        while(n>0){
            f=1;
            for(int i=1;i<=n%10;i++){
                f=f*i;
            }
            sum=sum+f;
            // System.out.println(sum);
            n=n/10;
            
            // System.out.println(n);
        }
        if(sum==k){
            System.out.println(k+"is strong no");
        }else{
            System.out.println(k+"is not strongno");
          }


    }
}
//148 is strong no 1!+4!+8!=148