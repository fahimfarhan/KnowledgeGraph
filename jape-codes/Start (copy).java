package japeactionclasses; 
 3  import gate.*;
 4  import java.io.*;
 5  import java.util.*;
 6  import gate.util.*;
 7  import gate.jape.*;
 8  import gate.creole.ontology.*;
 9    // JAPE Source: file:/home/fahimfarhan/Codes/Thesis-Codes/KnowledgeGraph/Ignore/module-6/hands-on/jape/resources/simple.jape:9
10   import static gate.Utils.*; 
11  public class SimpleListEntitiesActionClass672
12  implements java.io.Serializable, gate.jape.RhsAction { 
13    private gate.jape.ActionContext ctx;
14    public java.lang.String ruleName() { return "ListEntities"; }
15    public java.lang.String phaseName() { return "Simple"; }
16    public void setActionContext(gate.jape.ActionContext ac) { ctx = ac; }
17    public gate.jape.ActionContext getActionContext() { return ctx; }
18    public void doit(gate.Document doc, 
19                     java.util.Map<java.lang.String, gate.AnnotationSet> bindings, 
20                     gate.AnnotationSet inputAS, gate.AnnotationSet outputAS, 
21                     gate.creole.ontology.Ontology ontology) throws gate.jape.JapeException {
22      gate.AnnotationSet entAnnots = bindings.get("ent"); 
23      if(entAnnots != null && entAnnots.size() != 0) { 
24  
25    // print to System.out the type and features of each annotation found
26    AnnotationSet ents = bindings.get("ent");
27    //int count = 0;  // kaj kore na
28    featureMap(1,'a');
29    for(Annotation e : ents){
30      //count++;    // kaj
31      System.out.println(FeatureMap.size());
32      System.out.println("Found "+e.getType()+" annotation");
33      System.out.println("Features "+e.getFeatures());
34    }
35  
36      }
37    }
38  }
