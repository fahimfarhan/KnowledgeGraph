```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV
import time
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def getVectorAnalysis(a,b):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform([str(a),str(b)])
    c = ((tfidf * tfidf.T).A)
    ret = (c[0][1])
    return ret


def getIntersectionTuples(u,e,v,i):
    input_str = str(u) + " , "+str(e) +" , " +str(v)
    try:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(CSV)
        query = """PREFIX db: <http://dbpedia.org/resource/>
                    select distinct * where {
                    ?s ?o db:"""+str(u)+""" . 
                    db:"""+str(v)+ """ ?o ?p .
                    }
                    LIMIT 200"""
        # print(query)
        sparql.setQuery(query)  # the previous query as a literal string

        result =  sparql.query().convert()
        result_str = str(result)
        res_array = result_str.split("\\n")
        
        after_vector_analysis = [] 
        temp123_count = 0
        for i in res_array:
            try:
                print("case# "+str(temp123_count))
                temp123_count = temp123_count+1
                temp123 = i
                temp123 = temp123.replace( "\"", "")
                temp123_array = temp123.split(",")
                ui = temp123_array[0]
                ui = ui[28:]
                print("u = "+ui+" "+u)

                vi = temp123_array[2]
                vi = vi[28:]
                print("v = "+vi+" "+v)
                uscore = getVectorAnalysis(ui,u)
                vscore = getVectorAnalysis(vi,v)
                print(str(uscore)+" "+str(vscore))
                if( (uscore>0.4) and (vscore>0.4)):
                    print(i)
                    after_vector_analysis.append(i)
            except:
                pass
        s = "csv/tuple_"+str(i)+".csv"    
        fout = open(s, "w")
        for res in after_vector_analysis:
            fout.write(str(res)+" , "+str(input_str))
            fout.write("\n")
        fout.close()
    except Exception as x:
        print('sorry '+str(x))
        pass
    return 0


if __name__ == "__main__":
    file = open("SmallInput.txt","r")
    fileContent = file.readlines()
     
    lineCount=0
    for lines in fileContent:
        try:
            wordList = re.sub("[^\w]", " ",  lines).split()
            u = wordList[0]
            e = wordList[1]
            v = wordList[2]
            getIntersectionTuples(u,e,v,lineCount)
            # print(u+" "+v)
        except:
            pass 
        finally:
            lineCount=lineCount+1
    file.close()
    pass

```
# INPUT 
Cristiano_Ronaldo sth Juventus
# OUTPUT
case# 0
u =  Cristiano_Ronaldo
v =  Juventus
0.0 0.0
case# 1
u = 1985 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 2
u = 2000s_(decade) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 3
u = Alan_Shearer Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 4
u = Alex_Ferguson Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 5
u = La_Liga Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 6
u = Chris_Eagles Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 7
u = Michael_Laudrup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 8
u = Yaya_Tour\xc3\xa9 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 9
u = Antonio_Di_Natale Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 10
u = Curl_(football) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 11
u = Darren_Fletcher Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 12
u = Filippo_Inzaghi Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 13
u = Gorka_Iraizoz Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 14
u = Javier_Hern\xc3\xa1ndez Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 15
u = Milad_Meydavoudi Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 16
u = Pep_Guardiola Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 17
u = Wink Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 18
u = \xc3\x81lvaro_Negredo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 19
u = James_Rodr\xc3\xadguez Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 20
u = 2009_Liga_Deportiva_Universitaria_de_Quito_season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 21
u = 2009_Peace_Cup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 22
u = 2010\xe2\x80\x9311_Real_Madrid_C.F._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 23
u = Academia_de_Talentos Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 24
u = Ballon_d\'Or_2004 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 25
u = Ballon_d\'Or_2005 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 26
u = Ballon_d\'Or_2006 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 27
u = Ballon_d\'Or_2007 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 28
u = Ballon_d\'Or_2008 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 29
u = Eurovision_Song_Contest_2016 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 30
u = FC_Porto_in_international_club_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 31
u = List_of_Hugo_video_games Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 32
u = Richard_Chai Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 33
u = Romelu_Lukaku Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 34
u = The_Late_Late_Show_(season_47) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 35
u = Steve_McManaman Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 36
u = Trofeo_Alfredo_Di_St\xc3\xa9fano Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 37
u = 2003\xe2\x80\x9304_in_English_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 38
u = 2015_UEFA_Champions_League_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 39
u = 2015\xe2\x80\x9316_UEFA_Champions_League Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 40
u = 2016_UEFA_Champions_League_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 41
u = 2014_Copa_del_Rey_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 42
u = 2014\xe2\x80\x9315_La_Liga Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 43
u = 2014\xe2\x80\x9315_Liverpool_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 44
u = 2014\xe2\x80\x9315_UEFA_Champions_League_group_stage Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 45
u = Anwar_El_Ghazi Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 46
u = Brazil_at_the_2010_FIFA_World_Cup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 47
u = Iran_at_the_2006_FIFA_World_Cup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 48
u = Manchester_derby Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 49
u = Pro_Evolution_Soccer_2008 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 50
u = Rabona Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 51
u = Ricardo_Rodr\xc3\xadguez_(footballer) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 52
u = UEFA_Club_Football_Awards Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 53
u = UEFA_Club_Footballer_of_the_Year Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 54
u = UEFA_Euro_2016_qualifying_Group_I Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 55
u = Battle_of_the_Buffet Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 56
u = Region_of_Murcia_autonomous_football_team Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 57
u = 2003\xe2\x80\x9304_Portsmouth_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 58
u = 2003\xe2\x80\x9304_Tottenham_Hotspur_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 59
u = 2007\xe2\x80\x9308_Blackburn_Rovers_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 60
u = Premier_League_records_and_statistics Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 61
u = Arsenal_F.C._in_European_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 62
u = Chelsea_F.C._in_European_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 63
u = 2006\xe2\x80\x9307_FA_Premier_League Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 64
u = Ashley_Young Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 65
u = Adriano_(footballer Cristiano_Ronaldo
v = wikiPageWikiLink Juventus
0.0 0.0
case# 66
u = Claudio_Bravo_(footballer) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 67
u = Duda_(Portuguese_footballer) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 68
u = Elsa_Pataky Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 69
u = Madeira_Airport Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 70
u = Marcelo_(footballer Cristiano_Ronaldo
v = wikiPageWikiLink Juventus
0.0 0.0
case# 71
u = Mesut_\xc3\x96zil Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 72
u = List_of_Portuguese_people Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 73
u = Rivellino Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 74
u = Giourkas_Seitaridis Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 75
u = Jimmy_Jump Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 76
u = Wes_Brown Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 77
u = 2015\xe2\x80\x9316_La_Liga Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 78
u = 2011_Copa_del_Rey_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 79
u = 2013_Copa_del_Rey_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 80
u = 2013\xe2\x80\x9314_UEFA_Champions_League_group_stage Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 81
u = 2014\xe2\x80\x9315_Copa_del_Rey Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 82
u = 2014\xe2\x80\x9315_UEFA_Champions_League_knockout_phase Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 83
u = Battle_of_Nuremberg_(2006_FIFA_World_Cup) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 84
u = England_national_football_team_results_\xe2\x80\x93_2000s Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 85
u = Nolito Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 86
u = Rapha\xc3\xabl_Guerreiro Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 87
u = Ronaldo_(film) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 88
u = CR9 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 89
u = 2003\xe2\x80\x9304_FA_Cup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 90
u = 2007\xe2\x80\x9308_Everton_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 91
u = 2007\xe2\x80\x9308_Olympique_Lyonnais_season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 92
u = UEFA_Euro_2004_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 93
u = 2006\xe2\x80\x9307_Manchester_City_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 94
u = 2009\xe2\x80\x9310_Juventus_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 95
u = 2009\xe2\x80\x9310_Real_Madrid_C.F._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 96
u = 2009\xe2\x80\x9310_in_English_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 97
u = June_2009_in_sports Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 98
u = Katherine_Lynch Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 99
u = 2012_Golden_Globes_(Portugal) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 100
u = Kazakhstan_national_football_team_results Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 101
u = Nompumelelo_Nyandeni Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 102
u = UEFA_Euro_2012_statistics Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 103
u = 2004\xe2\x80\x9305_Newcastle_United_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 104
u = 2004\xe2\x80\x9305_Southampton_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 105
u = 2006\xe2\x80\x9307_Aston_Villa_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 106
u = 2010\xe2\x80\x9311_Sevilla_FC_season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 107
u = Alcorconazo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 108
u = Angola_at_the_FIFA_World_Cup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 109
u = North_Korea_at_the_FIFA_World_Cup Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 110
u = 2006\xe2\x80\x9307_Everton_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 111
u = 2006\xe2\x80\x9307_Portsmouth_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 112
u = 2011_Los_Angeles_Galaxy_season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 113
u = Peter_Lim Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 114
u = 2011\xe2\x80\x9312_Olympique_Lyonnais_season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 115
u = Filip_Kne\xc5\xbeevi\xc4\x87 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 116
u = 2006_FIFA_World_Cup_disciplinary_record Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 117
u = Globe_Soccer_Awards Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 118
u = Henry_Javier_Hern\xc3\xa1ndez Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 119
u = Premier_League_Player_of_the_Season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 120
u = List_of_sex_symbols Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 121
u = Buyout_clause Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 122
u = Cristaino_ronaldo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 123
u = Anders_Lindegaard Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 124
u = Facebook Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 125
u = Gael_Garc\xc3\xada_Bernal Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 126
u = Gareth_Bale Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 127
u = Header_(association_football) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 128
u = Jack_Lester Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 129
u = James_Morrison_(footballer) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 130
u = Lu\xc3\xads_Figo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 131
u = Michael_Murphy_(Gaelic_footballer) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 132
u = Petr_\xc4\x8cech Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 133
u = Sporting_Clube_de_Portugal Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 134
u = TAG_Heuer Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 135
u = Thiago_Silva Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 136
u = Tomahawk Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 137
u = UEFA_Financial_Fair_Play_Regulations Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 138
u = Virat_Kohli Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 139
u = Aly_Cissokho Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 140
u = Jean-Claude_Thibaut Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 141
u = Arjen_Robben Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 142
u = Corner_kick Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 143
u = Nutmeg_(football) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 144
u = Secret_Story_3_(Portugal) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 145
u = UEFA_Team_of_the_Year Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 146
u = Action_hero Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 147
u = Association_football_tactics_and_skills Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 148
u = Hungary_national_football_team Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 149
u = List_of_teetotalers Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 150
u = UEFA_Euro_2008 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 151
u = List_of_Real_Madrid_C.F._players Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 152
u = Real_Madrid_C.F._in_European_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 153
u = Eus\xc3\xa9bio Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 154
u = Gonzalo_Higua\xc3\xadn Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 155
u = List_of_English_football_champions Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 156
u = List_of_Real_Madrid_C.F._records_and_statistics Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 157
u = List_of_Real_Madrid_C.F._seasons Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 158
u = L\xc3\xaa_C\xc3\xb4ng_Vinh Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 159
u = UEFA_Euro_2008_Group_A Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 160
u = 2004_FA_Cup_Final Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 161
u = Dessie_Baker Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 162
u = Luiz_Adriano Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 163
u = Nicol\xc3\xa1s_Mill\xc3\xa1n Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 164
u = Nigel_Pearson Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 165
u = UEFA_Euro_2008_qualifying_Group_A Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 166
u = 2006\xe2\x80\x9307_A.C._Milan_season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 167
u = FWA_Footballer_of_the_Year Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 168
u = Football_boot Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 169
u = 2006\xe2\x80\x9307_Bolton_Wanderers_F.C._season Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 170
u = 2008_FIFA_Club_World_Cup_squads Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 171
u = 2008\xe2\x80\x9309_UEFA_Champions_League_knockout_phase Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 172
u = Eddie_Odhiambo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 173
u = Numeronym Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 174
u = 2004\xe2\x80\x9305_in_Portuguese_football Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 175
u = C_Ronaldo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 176
u = Cronaldo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 177
u = List_of_Manchester_United_F.C._seasons Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 178
u = CR7 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 179
u = History_of_Southend_United_F.C. Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 180
u = Chris_Ronaldo Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 181
u = David_Beckham Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 182
u = February_5 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 183
u = Madeira Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 184
u = Manchester_United_F.C. Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 185
u = Pel\xc3\xa9 Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 186
u = Portugal Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 187
u = Premier_League Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 188
u = Real_Madrid_C.F. Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 189
u = BBC_(disambiguation) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 190
u = Didi_(footballer) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 191
u = FIFA_Pusk\xc3\xa1s_Award Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 192
u = Florentino_P\xc3\xa9rez Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 193
u = Jos\xc3\xa9_Mourinho Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 194
u = Karim_Benzema Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 195
u = Luis_Su\xc3\xa1rez Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 196
u = Mark_Simpson_(journalist) Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 197
u = Mercedes-Benz_SLS_AMG Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 198
u = North_Korea_national_football_team Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 199
u = Ricardo_Carvalho Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 200
u = Ricardo_Quaresma Cristiano_Ronaldo
v = Juventus_F.C. Juventus
0.0 0.0
case# 201
u =  Cristiano_Ronaldo

# INPUT 
Cristiano sth Madrid
# OUTPUT 
case# 0
u =  Cristiano
v =  Madrid
0.0 0.0
case# 1
u = Cristiano_(given_name) Cristiano
v = Antonio_Stradivari Madrid
0.0 0.0
case# 2
u = Cristiano_(given_name) Cristiano
v = Autonomous_communities_of_Spain Madrid
0.0 0.0
case# 3
u = Cristiano_(given_name) Cristiano
v = Business Madrid
0.0 0.0
case# 4
u = Cristiano_(given_name) Cristiano
v = Business_school Madrid
0.0 0.0
case# 5
u = Cristiano_(given_name) Cristiano
v = Francis_I_of_France Madrid
0.0 0.0
case# 6
u = Cristiano_(given_name) Cristiano
v = Hieronymus_Bosch Madrid
0.0 0.0
case# 7
u = Cristiano_(given_name) Cristiano
v = High-speed_rail Madrid
0.0 0.0
case# 8
u = Cristiano_(given_name) Cristiano
v = La_Liga Madrid
0.0 0.0
case# 9
u = Cristiano_(given_name) Cristiano
v = Local_government Madrid
0.0 0.0
case# 10
u = Cristiano_(given_name) Cristiano
v = Master_of_Business_Administration Madrid
0.0 0.0
case# 11
u = Cristiano_(given_name) Cristiano
v = Museum Madrid
0.0 0.0
case# 12
u = Cristiano_(given_name) Cristiano
v = Operetta Madrid
0.0 0.0
case# 13
u = Cristiano_(given_name) Cristiano
v = Pension_fund Madrid
0.0 0.0
case# 14
u = Cristiano_(given_name) Cristiano
v = Postal_code Madrid
0.0 0.0
case# 15
u = Cristiano_(given_name) Cristiano
v = Salvador_Dal\xc3\xad Madrid
0.0 0.0
case# 16
u = Cristiano_(given_name) Cristiano
v = Standard_of_living Madrid
0.0 0.0
case# 17
u = Cristiano_(given_name) Cristiano
v = Telef\xc3\xb3nica Madrid
0.0 0.0
case# 18
u = Cristiano_(given_name) Cristiano
v = Tennis Madrid
0.0 0.0
case# 19
u = Cristiano_(given_name) Cristiano
v = Tourism Madrid
0.0 0.0
case# 20
u = Cristiano_(given_name) Cristiano
v = Vandals Madrid
0.0 0.0
case# 21
u = Cristiano_(given_name) Cristiano
v = Visigoths Madrid
0.0 0.0
case# 22
u = Cristiano_(given_name) Cristiano
v = Western_Europe Madrid
0.0 0.0
case# 23
u = Cristiano_(given_name) Cristiano
v = World_Tourism_Organization Madrid
0.0 0.0
case# 24
u = Cristiano_(given_name) Cristiano
v = Zarzuela Madrid
0.0 0.0
case# 25
u = Cristiano_(given_name) Cristiano
v = Alcalde Madrid
0.0 0.0
case# 26
u = Cristiano_(given_name) Cristiano
v = Food_processing Madrid
0.0 0.0
case# 27
u = Cristiano_(given_name) Cristiano
v = Seating_capacity Madrid
0.0 0.0
case# 28
u = Cristiano_(given_name) Cristiano
v = UNESCO Madrid
0.0 0.0
case# 29
u = Cristiano_(given_name) Cristiano
v = Zoo_Aquarium_de_Madrid Madrid
0.0 0.0
case# 30
u = Cristiano_(given_name) Cristiano
v = Agencia_Estatal_de_Meteorolog\xc3\xada Madrid
0.0 0.0
case# 31
u = Cristiano_(given_name) Cristiano
v = Boadilla_del_Monte Madrid
0.0 0.0
case# 32
u = Cristiano_(given_name) Cristiano
v = CaixaForum_Madrid Madrid
0.0 0.0
case# 33
u = Cristiano_(given_name) Cristiano
v = Caja_M\xc3\xa1gica Madrid
0.0 0.0
case# 34
u = Cristiano_(given_name) Cristiano
v = Chamart\xc3\xadn_Symphony_Orchestra Madrid
0.0 0.0
case# 35
u = Cristiano_(given_name) Cristiano
v = Community_of_Madrid_Orchestra Madrid
0.0 0.0
case# 36
u = Cristiano_(given_name) Cristiano
v = National_Auditorium_of_Music Madrid
0.0 0.0
case# 37
u = Cristiano_(given_name) Cristiano
v = Saint_Louis_University_Madrid_Campus Madrid
0.0 0.0
case# 38
u = Cristiano_(given_name) Cristiano
v = St._Michael\'s_Basilica_(Madrid) Madrid
0.0 0.37997836159100784
case# 39
u = Cristiano_(given_name) Cristiano
v = Plaza_Mayor Madrid
0.0 0.0
case# 40
u = Cristiano_(given_name) Cristiano
v = Leopoldo_O\'Donnell Madrid
0.0 0.0
case# 41
u = Cristiano_(given_name) Cristiano
v = Convent_of_the_Salesas_Reales Madrid
0.0 0.0
case# 42
u = Cristiano_(given_name) Cristiano
v = Our_Lady_of_Montserrat_Church Madrid
0.0 0.0
case# 43
u = Cristiano_(given_name) Cristiano
v = Santa_Cruz_Palace Madrid
0.0 0.0
case# 44
u = Cristiano_(given_name) Cristiano
v = El_Busc\xc3\xb3n Madrid
0.0 0.0
case# 45
u = Cristiano_(given_name) Cristiano
v = Jos\xc3\xa9_Grases_Riera Madrid
0.0 0.0
case# 46
u = Cristiano_(given_name) Cristiano
v = Cervantes_Institute Madrid
0.0 0.0
case# 47
u = Cristiano_(given_name) Cristiano
v = Basilica_of_San_Francisco_el_Grande_(Madrid) Madrid
0.0 0.5797386715376657
case# 48
u = Cristiano_(given_name) Cristiano
v = Triple_Crown_in_Basketball Madrid
0.0 0.0
case# 49
u = Cristiano_(given_name) Cristiano
v = Administration_(business) Madrid
0.0 0.0
case# 50
u = Cristiano_(given_name) Cristiano
v = R\xc3\xado_de_La_Plata_Bank Madrid
0.0 0.0
case# 51
u = Cristiano_(given_name) Cristiano
v = Category:Madrid Madrid
0.0 0.5797386715376657
case# 52
u = Cristiano_(given_name) Cristiano
v = European_University_of_Madrid Madrid
0.0 0.0
case# 53
u = Cristiano_(given_name) Cristiano
v = Fuenlabrada Madrid
0.0 0.0
case# 54
u = Cristiano_(given_name) Cristiano
v = RTVE_Symphony_Orchestra Madrid
0.0 0.0
case# 55
u = Cristiano_(given_name) Cristiano
v = Real_Jard\xc3\xadn_Bot\xc3\xa1nico_de_Madrid Madrid
0.0 0.0
case# 56
u = Cristiano_(given_name) Cristiano
v = Alcorc\xc3\xb3n Madrid
0.0 0.0
case# 57
u = Cristiano_(given_name) Cristiano
v = C40_Cities_Climate_Leadership_Group Madrid
0.0 0.0
case# 58
u = Cristiano_(given_name) Cristiano
v = Chamart\xc3\xadn_(Madrid) Madrid
0.0 0.37997836159100784
case# 59
u = Cristiano_(given_name) Cristiano
v = Charles_III_University_of_Madrid Madrid
0.0 0.0
case# 60
u = Cristiano_(given_name) Cristiano
v = King_Juan_Carlos_University Madrid
0.0 0.0
case# 61
u = Cristiano_(given_name) Cristiano
v = National_Archaeological_Museum_of_Spain Madrid
0.0 0.0
case# 62
u = Cristiano_(given_name) Cristiano
v = Palacio_de_Deportes_de_la_Comunidad_de_Madrid Madrid
0.0 0.0
case# 63
u = Cristiano_(given_name) Cristiano
v = Modern_art Madrid
0.0 0.0
case# 64
u = Cristiano_(given_name) Cristiano
v = Seat_of_government Madrid
0.0 0.0
case# 65
u = Cristiano_(given_name) Cristiano
v = Teatro_Real Madrid
0.0 0.0
case# 66
u = Cristiano_(given_name) Cristiano
v = T\xc3\xado_Pepe Madrid
0.0 0.0
case# 67
u = Cristiano_(given_name) Cristiano
v = Rogier_van_der_Weyden Madrid
0.0 0.0
case# 68
u = Cristiano_(given_name) Cristiano
v = Lady_of_Baza Madrid
0.0 0.0
case# 69
u = Cristiano_(given_name) Cristiano
v = Spanish_miracle Madrid
0.0 0.0
case# 70
u = Cristiano_(given_name) Cristiano
v = Global_city Madrid
0.0 0.0
case# 71
u = Cristiano_(given_name) Cristiano
v = La_Movida_Madrile\xc3\xb1a Madrid
0.0 0.0
case# 72
u = Cristiano_(given_name) Cristiano
v = Linear_city Madrid
0.0 0.0
case# 73
u = Cristiano_(given_name) Cristiano
v = Spanish_Golden_Age Madrid
0.0 0.0
case# 74
u = Cristiano_(given_name) Cristiano
v = Spanish_royal_sites Madrid
0.0 0.0
case# 75
u = Cristiano_(given_name) Cristiano
v = Expressionist Madrid
0.0 0.0
case# 76
u = Cristiano_(given_name) Cristiano
v = St._Francis_of_Assisi Madrid
0.0 0.0
case# 77
u = Cristiano_(given_name) Cristiano
v = St._Paul\'s_Cathedral Madrid
0.0 0.0
case# 78
u = Cristiano_(given_name) Cristiano
v = American_continent Madrid
0.0 0.0
case# 79
u = Cristiano_(given_name) Cristiano
v = House_of_Austria Madrid
0.0 0.0
case# 80
u = Cristiano_(given_name) Cristiano
v = Ir\xc3\xban Madrid
0.0 0.0
case# 81
u = Cristiano_(given_name) Cristiano
v = Raphael_Sanzio Madrid
0.0 0.0
case# 82
u = Cristiano_(given_name) Cristiano
v = WTA_Tour Madrid
0.0 0.0
case# 83
u = Cristiano_(given_name) Cristiano
v = Mar\xc3\xada_Guerrero Madrid
0.0 0.0
case# 84
u = Cristiano_(given_name) Cristiano
v = San_Pedro_el_Real Madrid
0.0 0.0
case# 85
u = Cristiano_(given_name) Cristiano
v = The_Judgement_of_Paris_(Rubens) Madrid
0.0 0.0
case# 86
u = Cristiano_(given_name) Cristiano
v = Virgin_of_Almudena Madrid
0.0 0.0
case# 87
u = Cristiano_(given_name) Cristiano
v = Catholic_Kings Madrid
0.0 0.0
case# 88
u = Cristiano_(given_name) Cristiano
v = St._Januarius Madrid
0.0 0.0
case# 89
u = Cristiano_(given_name) Cristiano
v = Romanians_in_Spain Madrid
0.0 0.0
case# 90
u = Cristiano_(given_name) Cristiano
v = Cervantes Madrid
0.0 0.0
case# 91
u = Cristiano_(given_name) Cristiano
v = San_Isidro_Labrador Madrid
0.0 0.0
case# 92
u = Cristiano_(given_name) Cristiano
v = Brussels_tapestry Madrid
0.0 0.0
case# 93
u = Cristiano_(given_name) Cristiano
v = Pompeo_Leoni Madrid
0.0 0.0
case# 94
u = Cristiano_(given_name) Cristiano
v = File:Museo_del_Prado_2016_(25185969599).jpg Madrid
0.0 0.0
case# 95
u = Cristiano_(given_name) Cristiano
v = Ancient_Greece Madrid
0.0 0.0
case# 96
u = Cristiano_(given_name) Cristiano
v = Culture Madrid
0.0 0.0
case# 97
u = Cristiano_(given_name) Cristiano
v = C\xc3\xadrculo_de_Bellas_Artes Madrid
0.0 0.0
case# 98
u = Cristiano_(given_name) Cristiano
v = Diego_Vel\xc3\xa1zquez Madrid
0.0 0.0
case# 99
u = Cristiano_(given_name) Cristiano
v = Economic_growth Madrid
0.0 0.0
case# 100
u = Cristiano_(given_name) Cristiano
v = Kane_(wrestler) Madrid
0.0 0.0
case# 101
u = Cristiano_(given_name) Cristiano
v = K\xc3\xb6ppen_climate_classification Madrid
0.0 0.0
case# 102
u = Cristiano_(given_name) Cristiano
v = Museo_Nacional_de_Antropolog\xc3\xada Madrid
0.0 0.0
case# 103
u = Cristiano_(given_name) Cristiano
v = People\'s_Party_(Spain) Madrid
0.0 0.0
case# 104
u = Cristiano_(given_name) Cristiano
v = Population_growth Madrid
0.0 0.0
case# 105
u = Cristiano_(given_name) Cristiano
v = Private_university Madrid
0.0 0.0
case# 106
u = Cristiano_(given_name) Cristiano
v = Real_Academia_de_Bellas_Artes_de_San_Fernando Madrid
0.0 0.0
case# 107
u = Cristiano_(given_name) Cristiano
v = Spanish_Air_Force Madrid
0.0 0.0
case# 108
u = Cristiano_(given_name) Cristiano
v = Trade_fair Madrid
0.0 0.0
case# 109
u = Cristiano_(given_name) Cristiano
v = United_Left_(Spain) Madrid
0.0 0.0
case# 110
u = Cristiano_(given_name) Cristiano
v = Autonomous_University_of_Madrid Madrid
0.0 0.0
case# 111
u = Cristiano_(given_name) Cristiano
v = Chueca Madrid
0.0 0.0
case# 112
u = Cristiano_(given_name) Cristiano
v = Comillas_Pontifical_University Madrid
0.0 0.0
case# 113
u = Cristiano_(given_name) Cristiano
v = Instituto_Cervantes Madrid
0.0 0.0
case# 114
u = Cristiano_(given_name) Cristiano
v = Plaza_de_Cibeles Madrid
0.0 0.0
case# 115
u = Cristiano_(given_name) Cristiano
v = Plaza_de_Oriente Madrid
0.0 0.0
case# 116
u = Cristiano_(given_name) Cristiano
v = Puerta_de_Alcal\xc3\xa1 Madrid
0.0 0.0
case# 117
u = Cristiano_(given_name) Cristiano
v = Technical_University_of_Madrid Madrid
0.0 0.0
case# 118
u = Cristiano_(given_name) Cristiano
v = University_of_Alcal\xc3\xa1 Madrid
0.0 0.0
case# 119
u = Cristiano_(given_name) Cristiano
v = Vicente_Calder\xc3\xb3n_Stadium Madrid
0.0 0.0
case# 120
u = Cristiano_(given_name) Cristiano
v = Civilian_casualties Madrid
0.0 0.0
case# 121
u = Cristiano_(given_name) Cristiano
v = Peninsular_War Madrid
0.0 0.0
case# 122
u = Cristiano_(given_name) Cristiano
v = Alonso_Berruguete Madrid
0.0 0.0
case# 123
u = Cristiano_(given_name) Cristiano
v = Joanna_of_Austria Madrid
0.0 0.0
case# 124
u = Cristiano_(given_name) Cristiano
v = Las_Acacias_(Madrid) Madrid
0.0 0.5797386715376657
case# 125
u = Cristiano_(given_name) Cristiano
v = Palace_of_Longoria Madrid
0.0 0.0
case# 126
u = Cristiano_(given_name) Cristiano
v = Spanish_Civil_War Madrid
0.0 0.0
case# 127
u = Cristiano_(given_name) Cristiano
v = Fuencarral-El_Pardo Madrid
0.0 0.0
case# 128
u = Cristiano_(given_name) Cristiano
v = Teatro_Monumental Madrid
0.0 0.0
case# 129
u = Cristiano_(given_name) Cristiano
v = Water_supply Madrid
0.0 0.0
case# 130
u = Cristiano_(given_name) Cristiano
v = Arganzuela Madrid
0.0 0.0
case# 131
u = Cristiano_(given_name) Cristiano
v = Hortaleza Madrid
0.0 0.0
case# 132
u = Cristiano_(given_name) Cristiano
v = Moncloa-Aravaca Madrid
0.0 0.0
case# 133
u = Cristiano_(given_name) Cristiano
v = Oscar_II_Coast Madrid
0.0 0.0
case# 134
u = Cristiano_(given_name) Cristiano
v = Puente_de_Vallecas Madrid
0.0 0.0
case# 135
u = Cristiano_(given_name) Cristiano
v = Usera Madrid
0.0 0.0
case# 136
u = Cristiano_(given_name) Cristiano
v = Villa_de_Vallecas Madrid
0.0 0.0
case# 137
u = Cristiano_(given_name) Cristiano
v = Bullfighting Madrid
0.0 0.0
case# 138
u = Cristiano_(given_name) Cristiano
v = Madrid_Conference_of_1991 Madrid
0.0 0.0
case# 139
u = Cristiano_(given_name) Cristiano
v = Military_history Madrid
0.0 0.0
case# 140
u = Cristiano_(given_name) Cristiano
v = Chinese_people_in_Spain Madrid
0.0 0.0
case# 141
u = Cristiano_(given_name) Cristiano
v = Cold_semi-arid_climate Madrid
0.0 0.0
case# 142
u = Cristiano_(given_name) Cristiano
v = The_Dog_in_the_Manger Madrid
0.0 0.0
case# 143
u = Cristiano_(given_name) Cristiano
v = Churrigueresque Madrid
0.0 0.0
case# 144
u = Cristiano_(given_name) Cristiano
v = Zurbar\xc3\xa1n Madrid
0.0 0.0
case# 145
u = Cristiano_(given_name) Cristiano
v = Pantheon_(Rome) Madrid
0.0 0.0
case# 146
u = Cristiano_(given_name) Cristiano
v = Autov\xc3\xada Madrid
0.0 0.0
case# 147
u = Cristiano_(given_name) Cristiano
v = City_Council_of_Madrid Madrid
0.0 0.0
case# 148
u = Cristiano_(given_name) Cristiano
v = Rubens Madrid
0.0 0.0
case# 149
u = Cristiano_(given_name) Cristiano
v = Jose_de_Echegaray Madrid
0.0 0.0
case# 150
u = Cristiano_(given_name) Cristiano
v = Albrecht_D\xc3\xbcrer Madrid
0.0 0.0
case# 151
u = Cristiano_(given_name) Cristiano
v = Alfonso_XIII_of_Spain Madrid
0.0 0.0
case# 152
u = Cristiano_(given_name) Cristiano
v = Alicante Madrid
0.0 0.0
case# 153
u = Cristiano_(given_name) Cristiano
v = Anno_Domini Madrid
0.0 0.0
case# 154
u = Cristiano_(given_name) Cristiano
v = Apollo Madrid
0.0 0.0
case# 155
u = Cristiano_(given_name) Cristiano
v = Association_football Madrid
0.0 0.0
case# 156
u = Cristiano_(given_name) Cristiano
v = Athens Madrid
0.0 0.0
case# 157
u = Cristiano_(given_name) Cristiano
v = Auguste_Rodin Madrid
0.0 0.0
case# 158
u = Cristiano_(given_name) Cristiano
v = Barcelona Madrid
0.0 0.0
case# 159
u = Cristiano_(given_name) Cristiano
v = Basketball Madrid
0.0 0.0
case# 160
u = Cristiano_(given_name) Cristiano
v = Bayonne Madrid
0.0 0.0
case# 161
u = Cristiano_(given_name) Cristiano
v = Bear Madrid
0.0 0.0
case# 162
u = Cristiano_(given_name) Cristiano
v = Berlin Madrid
0.0 0.0
case# 163
u = Cristiano_(given_name) Cristiano
v = Bolivia Madrid
0.0 0.0
case# 164
u = Cristiano_(given_name) Cristiano
v = Bordeaux Madrid
0.0 0.0
case# 165
u = Cristiano_(given_name) Cristiano
v = Brazil Madrid
0.0 0.0
case# 166
u = Cristiano_(given_name) Cristiano
v = Brussels Madrid
0.0 0.0
case# 167
u = Cristiano_(given_name) Cristiano
v = Bulgaria Madrid
0.0 0.0
case# 168
u = Cristiano_(given_name) Cristiano
v = Bus Madrid
0.0 0.0
case# 169
u = Cristiano_(given_name) Cristiano
v = Caravaggio Madrid
0.0 0.0
case# 170
u = Cristiano_(given_name) Cristiano
v = Category:Capitals_in_Europe Madrid
0.0 0.0
case# 171
u = Cristiano_(given_name) Cristiano
v = Category:Populated_places_established_in_the_9th_century Madrid
0.0 0.0
case# 172
u = Cristiano_(given_name) Cristiano
v = Category:University_towns_in_Spain Madrid
0.0 0.0
case# 173
u = Cristiano_(given_name) Cristiano
v = Central_bank Madrid
0.0 0.0
case# 174
u = Cristiano_(given_name) Cristiano
v = Computer_science Madrid
0.0 0.0
case# 175
u = Cristiano_(given_name) Cristiano
v = Cycling Madrid
0.0 0.0
case# 176
u = Cristiano_(given_name) Cristiano
v = Dominican_Republic Madrid
0.0 0.0
case# 177
u = Cristiano_(given_name) Cristiano
v = Don_Quixote Madrid
0.0 0.0
case# 178
u = Cristiano_(given_name) Cristiano
v = Econometrics Madrid
0.0 0.0
case# 179
u = Cristiano_(given_name) Cristiano
v = Economics Madrid
0.0 0.0
case# 180
u = Cristiano_(given_name) Cristiano
v = Education Madrid
0.0 0.0
case# 181
u = Cristiano_(given_name) Cristiano
v = England Madrid
0.0 0.0
case# 182
u = Cristiano_(given_name) Cristiano
v = Entertainment Madrid
0.0 0.0
case# 183
u = Cristiano_(given_name) Cristiano
v = Equatorial_Guinea Madrid
0.0 0.0
case# 184
u = Cristiano_(given_name) Cristiano
v = European_Union Madrid
0.0 0.0
case# 185
u = Cristiano_(given_name) Cristiano
v = Fashion Madrid
0.0 0.0
case# 186
u = Cristiano_(given_name) Cristiano
v = Finance Madrid
0.0 0.0
case# 187
u = Cristiano_(given_name) Cristiano
v = Francisco_Franco Madrid
0.0 0.0
case# 188
u = Cristiano_(given_name) Cristiano
v = Francisco_Goya Madrid
0.0 0.0
case# 189
u = Cristiano_(given_name) Cristiano
v = Geology Madrid
0.0 0.0
case# 190
u = Cristiano_(given_name) Cristiano
v = Guatemala_City Madrid
0.0 0.0
case# 191
u = Cristiano_(given_name) Cristiano
v = Higher_education Madrid
0.0 0.0
case# 192
u = Cristiano_(given_name) Cristiano
v = History_of_Islam Madrid
0.0 0.0
case# 193
u = Cristiano_(given_name) Cristiano
v = Holiday Madrid
0.0 0.0
case# 194
u = Cristiano_(given_name) Cristiano
v = Iberian_Peninsula Madrid
0.0 0.0
case# 195
u = Cristiano_(given_name) Cristiano
v = India Madrid
0.0 0.0
case# 196
u = Cristiano_(given_name) Cristiano
v = Industry Madrid
0.0 0.0
case# 197
u = Cristiano_(given_name) Cristiano
v = Insurance Madrid
0.0 0.0
case# 198
u = Cristiano_(given_name) Cristiano
v = Italy Madrid
0.0 0.0
case# 199
u = Cristiano_(given_name) Cristiano
v = Juan_Gris Madrid
0.0 0.0
case# 200
u = Cristiano_(given_name) Cristiano
v = Latin Madrid
0.0 0.0
case# 201
u =  Cristiano