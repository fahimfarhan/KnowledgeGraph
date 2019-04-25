

def endgameRelatedness(num):
    filename = "score/score_"+str(num)+".csv"
    fin = open(filename,'r')
    content = fin.readlines() 
    maximus = 0.0
    maximusLine = ""
    for lines in content:
        temp = lines.split(";")
        currScore = float(temp[0])
        if(currScore>maximus):
            maximus = currScore
            maximusLine = lines
        

    filename = "finalOutputR.csv"
    fout = open(filename, "a") 
    fout.write(maximusLine)
    # print(writeLine)
    fout.close()

def endgameVector(num):
    filename = "score/score_"+str(num)+".csv"
    fin = open(filename,'r')
    content = fin.readlines() 
    maximus = 0.0
    maximusLine = ""
    for lines in content:
        temp = lines.split(";")
        currScore = float(temp[1])
        if( (currScore==0.0) or (currScore>=0.9999999999999998) ):
            pass
        elif(currScore>maximus):
            maximus = currScore
            maximusLine = lines
    

    filename = "finalOutputV.csv"
    fout = open(filename, "a") 
    fout.write(maximusLine)
    # print(writeLine)
    fout.close()

if __name__ == "__main__":
    for i in range(1,500):
        try:
            endgameRelatedness(i)
            endgameVector(i)
        except:
            pass
    pass
