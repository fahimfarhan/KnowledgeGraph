import java.util.*;

public static final class Singleton{
        
    private static volatile Singleton singleton = new Singleton();

    private Singleton(){
        System.out.println("creating...!!");
            
    }

    public static Singleton getInstance(){
        if(singleton == null){
            singleton = new Singleton();
            System.out.println("1. This is from new singleton!\n");
            return singleton;
        }else{
            System.out.println("2. This is from old singleton!\n");
            return singleton;
        }
        //return singleton;
    }
}