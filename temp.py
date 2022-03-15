import tweet
import geo
import json
import colors
import us_states
import state
import country
import re
from geo import GeoPosition
from tweet import Tweet
from collections import Counter
a=open("/Users/GUMI01/Desktop/tweets_with_time_2.json","r")
c=open("/Users/GUMI01/Desktop/tweets_with_time.json","r")
b=open("/Users/GUMI01/Desktop/sentiments.csv","r") 
d=open("/Users/GUMI01/Desktop/tweets_with_time_3.json","r")
e=open("/Users/GUMI01/Desktop/tweets_with_time_4.json","r")
konosuba = open("/Users/GUMI01/Desktop/color_map.pdf","wb")
a.readline()
b.readline()
c.readline()
d.readline()
e.readline()
score_word = {}
scorelist = []
scorelist2 = []
scorelist3 = []
scorelist4 = []
scorelist5 = []
de_weight = []
de_geolist = []
de_numberlist = []
score = 0
for sentiments in b:
    sentiments = sentiments.strip("\n")
    keys = sentiments.split(",")
    score_word.update({keys[0]: float(keys[1])})
my_dict = {}
select=[]
select_word = []
select_word2 = []
select_word3 = []
goushilist = []
shabilist = []
angrylist =[]
bngrylist = []
geolist = []
geonumberlist = []
geofinallist = []

for line in a:  
    decodes=json.loads(line) 
    my_dict = {"text":decodes[u"text"], "time":decodes[u"created_at"], "coordinates":decodes[u"coordinates"]}
    select.append(my_dict["text"])
    geolist.append(my_dict["coordinates"])

for line in c:  
    decodes=json.loads(line) 
    my_dict = {"text":decodes[u"text"], "time":decodes[u"created_at"], "coordinates":decodes[u"coordinates"]}
    select.append(my_dict["text"])
    geolist.append(my_dict["coordinates"])

for line in d:  
    decodes=json.loads(line) 
    my_dict = {"text":decodes[u"text"], "time":decodes[u"created_at"], "coordinates":decodes[u"coordinates"]}
    select.append(my_dict["text"])
    geolist.append(my_dict["coordinates"])

for line in e:  
    decodes=json.loads(line) 
    my_dict = {"text":decodes[u"text"], "time":decodes[u"created_at"], "coordinates":decodes[u"coordinates"]}
    select.append(my_dict["text"])
    geolist.append(my_dict["coordinates"])    
for word in select:
    word = str(word)
    select_word2 = word.split(" ")
    select_word3.append(select_word2)
    
for char in select_word3:
    goushilist.append(char)
    
for gunduzi in goushilist:
    shabilist = []
    for bitch in gunduzi:
        shabilist.append(bitch.lower())
    angrylist.append(shabilist)
    
ask = str.lower(input("Please enter the key word: "))

for wtf in angrylist:
    for sb in wtf:
        if ask in sb:
            bngrylist.append(wtf)
            geonumberlist.append(angrylist.index(wtf))
            
for sky in geonumberlist: #去重
    if sky not in de_numberlist:
        de_numberlist.append(sky)

for bitch in de_numberlist:
    geofinallist.append(geolist[bitch])
'''

for us in geofinallist: #去重
    if us not in de_geolist:
        de_geolist.append(us)
'''

for we in bngrylist: #去重
    if we not in de_weight:
        de_weight.append(we)

for thing in de_weight:
    scorelist = []
    for sb in thing:
        if sb in score_word:
            scorelist.append(score_word[sb])
    scorelist2.append(scorelist)

for miku in scorelist2:
    scorelist3 = []
    for hatsune in miku:
        float(hatsune)
        scorelist3.append(hatsune)
    scorelist4.append(scorelist3)

for jerry in scorelist4:
    score = 0
    n =0
    score = sum(jerry)
    scorelist5.append(score)
statelist1 = []
statelist2 = []
distance = []
distance_final = []
distance_2final = []
distance_3final = []
statelist = []
states = state.load_states()
for state in states:
    statelist1.append(geo.GeoPosition.latitude(state._computeCentroid()))
    statelist2.append(geo.GeoPosition.longitude(state._computeCentroid()))    
for fengwei in geofinallist:
    distance = []
    for n in range(51):
        distance.append(GeoPosition(fengwei[1],fengwei[0]).distance(GeoPosition(statelist1[n],statelist2[n])))
        n = n+1
    distance_final.append(distance)
    
for sky in distance_final:
    shi = min(sky)
    distance_2final.append(sky.index(shi))
for state in states:
    statelist.append(state.abbrev())
    
for io in distance_2final:
    distance_3final.append(statelist[io])
  
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
colorr = []
p = 0
nu = 0
for p in range(len(distance_3final)):
    list1 = []
    list1.append(scorelist5[p])
    list1.append(distance_3final[p])
    list2.append(list1)
    
for xd in statelist:
    for xp in list2:
        if xd in xp:
            list3.append(xp[0])
            list4.append(xp[1])
H = Counter(list4)
list5 = [ [k,]*v for k,v in H.items()]

result = []
C = 0
for item in list5:
    item_len = len(item)
    list6.append(list3[C: C+item_len])
    C += item_len
for es in list6:
    z = sum(es)
    t = z/len(es)
    list7.append(t)

for se in list5:
    y = se[0]
    list8.append(y)

combine_list = [j for i in zip(list7,list8) for j in i]
for rt in combine_list:
    while nu <= len(combine_list)-1:
        list9 = []
        list9.append(combine_list[nu])
        list9.append(combine_list[nu+1])
        nu = nu+2
        list10.append(list9)

for clo in list10: 
    colorr.append(colors.get_sentiment_color(clo[0]))
usa = country.Country(states, 1200)
final_color = [j for i in zip(list8,colorr) for j in i]
color_len = 0
for tr in final_color:
    while color_len <= len(final_color)-1:
        list12 = []
        list12.append(final_color[color_len])
        list12.append(final_color[color_len+1])
        color_len = color_len+2
        list13.append(list12)
for olc in list13:
    usa.setFillColor(olc[0],olc[1])

a.close()
b.close()
c.close()
d.close()
e.close()
'''

for es in statelist:
    for zhang in list6:
        list8 = []
        if es in zhang:
            list7.append(zhang)
print(list7)
'''
'''
for es in list6:
    while un <= len(list6)-2:
        list7 = []
        list7.append(list6[un])
        list7.append(list6[un+1])
        un = un+2
        list8.append(list7)
print(list8)
'''


'''
C = Counter(list6)
list8 = [ [k,]*v for k,v in C.items()]
print(list8)
'''
'''
print(list2)
for ost in range(51):
    for xd in list2:
        if statelist[ost] in xd:
            list3.append(statelist[ost])
        list4.append(list3)
'''
'''
for xp in list2:
    for ost in range(51):
        list4= []
        if statelist[ost] in xp[1]:
            list3.append(xp)
        list4.append(list3)
print(list4)         
'''
'''
tweet1 = Tweet(my_dict["text"],my_dict["time"],my_dict["coordinates"])
'''