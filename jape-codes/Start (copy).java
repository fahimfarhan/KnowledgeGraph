package japeactionclasses; 
   import gate.*;
   import java.io.*;
   import java.util.*;
   import gate.util.*;
   import gate.jape.*;
   import gate.creole.ontology.*;
     // JAPE Source: file:/home/fahimfarhan/Codes/Thesis-Codes/KnowledgeGraph/Ignore/module-6/hands-on/jape/resources/simple.jape:9
   import static gate.Utils.*; 
  public class SimpleListEntitiesActionClass672
  implements java.io.Serializable, gate.jape.RhsAction { 
    private gate.jape.ActionContext ctx;
    public java.lang.String ruleName() { return "ListEntities"; }
    public java.lang.String phaseName() { return "Simple"; }
    public void setActionContext(gate.jape.ActionContext ac) { ctx = ac; }
    public gate.jape.ActionContext getActionContext() { return ctx; }
    public void doit(gate.Document doc, 
                     java.util.Map<java.lang.String, gate.AnnotationSet> bindings, 
                     gate.AnnotationSet inputAS, gate.AnnotationSet outputAS, 
                     gate.creole.ontology.Ontology ontology) throws gate.jape.JapeException {
      gate.AnnotationSet entAnnots = bindings.get("ent"); 
      if(entAnnots != null && entAnnots.size() != 0) { 
  
    // print to System.out the type and features of each annotation found
   AnnotationSet ents = bindings.get("ent");
    //int count = 0;  // kaj kore na
    featureMap(1,'a');
   for(Annotation e : ents){
      //count++;    // kaj
     System.out.println(FeatureMap.size());
     System.out.println("Found "+e.getType()+" annotation");
      System.out.println("Features "+e.getFeatures());
    }
 
     }
   }
  }
