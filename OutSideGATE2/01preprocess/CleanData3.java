import java.util.*;

public class CleanData3{
    public static void main(String[] Args){
        Scanner sc = new Scanner(System.in);
        String s1="", s2="", s3="";
        while(sc.hasNextLine()){
            s1 = sc.next(); s2=sc.next(); s3=sc.next();
            
            s1 = s1.substring(0, s1.length()-1);
            s2 = s2.substring(0, s2.length()-1);
            
            char ch;
            ch = s1.charAt(0);
            if(s1.length()>=3 && s3.length() >=3 ){
                
                if( (ch >='a') && (ch<='z') ){
                    String first =  "" + ch;
                    first = first.toUpperCase();
                    s1 = first + s1.substring(1);
                }
                ch = s3.charAt(0);
                if( (ch >='a') && (ch<='z') ){
                    String first =  "" + ch;
                    first = first.toUpperCase();
                    s3 = first + s3.substring(1);
                }

                System.out.println(s1+"  "+s2+"  "+s3);
            }
            

        }
        sc.close();
    }
}