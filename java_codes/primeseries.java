public class primeseries {
    public static void main(String...args){
        int n=20;
        for(int i=1;i<=n;i++){
            int c=0;
            for(int j=1;j<=i;j++){
                if(i%j==0){
                    c+=1;
                }
                
            }
            if(c==2){
                    System.out.print(" "+i);
                }
        }
    }
}
