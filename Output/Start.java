import java.util.*;
import javafx.util.Pair; 

public class Start{
    public static void main(String[] Args){
        Scanner sc = new Scanner(System.in);

        Map<String, Vector < Pair<String, String> > > mp = new TreeMap<>();
        System.out.println("\n\n------------ Tuple ----------\n\n");
        while(sc.hasNextLine()){
            String s = sc.nextLine();
            String[] a = s.split(",");
            String u,e,v;
            u = a[2].substring(3);
            e = a[3].substring(3);
            v = a[4].substring(3, a[4].length() - 1 ); 
            System.out.println("< "+u+" , "+e+" , "+v+" > ");
            Pair<String, String > p = new Pair<>(v,e);

            if(mp.containsKey(u)){
                mp.get(u).addElement(p);
            }else{
                Vector< Pair<String, String> > vector = new Vector<>();
                vector.addElement(p);
                mp.put(u,vector);
                
            }
        }
        System.out.println("\n\n------------ Linked List Representation ----------\n\n");
        for (String key : mp.keySet())  
        { 
            // search  for value 
            Vector< Pair<String, String> > vector = mp.get(key); 
            System.out.print(key+" --> ");
            Enumeration e = vector.elements();
            for(Pair<String, String> obj : vector) {
                System.out.print(" ( "+obj.getKey()+" | "+obj.getValue()+" ) --> ");
            } 
           
            System.out.println("|/|"); 
              
        } 


    }
}