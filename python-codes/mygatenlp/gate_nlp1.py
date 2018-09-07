
import itertools
import gatenlp


# annotation_file_path = "/path/to/annotation_file.xml"
annotation_file_path = "/home/fahimfarhan/Codes/Thesis-Codes/KnowledgeGraph/corpusExpDefaultANNIE/Kiddon11.pdf.xml"

annotation_file = gatenlp.AnnotationFile(annotation_file_path)

# Automatically links any annotation continuations to their continued annotations.
annotations = annotation_file.annotations

sentences = [
    annotation
    for annotation in annotations
    # The type is just a string pulled from the XML
    if annotation.type == "Sentence" # "Sentence"
]

# doubly links each annotation
gatenlp.dlink(sentences)

''' for sentence in sentences[1:5]:
    print(
        sentence.previous.id,
        sentence.id,
        sentence.next.id,
    )
'''
print("------------------------------")

# interval tree structure for querying overlaps
tree = annotation_file.interval_tree
for annotation in annotations:
    tree.add(annotation)

tokens = [
    annotation
    for annotation in annotations
    if annotation.type == "Token"
]

# An example of querying the interval tree
for token in sorted(tokens, key=lambda x: x.start_node)[20:50]:
    print(
        str(token.id).ljust(5),
        str(token.start_node).ljust(5),
        str(token.end_node).ljust(5),
        token.type.ljust(10),
        token.text,
    )
    for intersection in tree.search(token):
        if intersection != token:
            x = 0
            ''' 
            print(
                str(intersection.start_node).ljust(5),
                str(intersection.end_node).ljust(5),
                str(intersection.id).ljust(5),
                intersection.type.ljust(10),
                intersection.text,
            )
            '''
print("------------------------")

##########################################################


identifiers = [
    annotation
    for annotation in annotations
    if annotation.type == "Address"
]

# An example of querying the interval tree
for identifier in sorted(identifiers, key=lambda x: x.start_node)[20:50]:
    print(
        str(identifier.id).ljust(5),
        str(identifier.start_node).ljust(5),
        str(identifier.end_node).ljust(5),
        identifier.type.ljust(10),
        identifier.text,
    )
    for intersection in tree.search(identifier):
        if intersection != identifier:
            x = 0
            '''
            print(
                str(intersection.start_node).ljust(5),
                str(intersection.end_node).ljust(5),
                str(intersection.id).ljust(5),
                intersection.type.ljust(10),
                intersection.text,
            )
            '''
print('----------------------------')