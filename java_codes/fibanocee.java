public class fibanocee {
    public static void main(String...args){
        int a=0,b=1;
        System.out.print(" "+a);
        System.out.print(" "+b);
        int s=0;
        for(int i=2;i<=10;i++){
            s=a+b;
            System.out.print(" "+s);
            a=b;
            b=s;
        }
    }
}
