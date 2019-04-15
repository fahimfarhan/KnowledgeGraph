import java.util.*;

public class MyToLower4{
    public static void main(String[] Args){
        Scanner sc = new Scanner(System.in);
        String s;
        while(sc.hasNextLine()){
            s = sc.nextLine();
            s = s.toLowerCase();
            System.out.println(s);
        }

        sc.close();
    }
}