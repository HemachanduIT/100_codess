public class perfect_no {
 public static void main(String...args){
    int n=7;
    int sum=0;
    for(int i=1;i<n;i++){
        if(n%i==0){
            sum+=i;
        }
    }
    if(sum==n){
        System.out.println("the no"+n+"is a perfect no");
    }else{
                System.out.println("the no"+n+"is NOT A perfect no");

    }
 }
}
