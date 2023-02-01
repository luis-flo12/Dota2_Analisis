import requests, json, time, os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import figure

#Creamos una list que iremos llenando con los datos que queramos
db= []

for i in os.listdir('partidas'):
    file = open ('partidas'+ os.sep+ i)
    data = json.load(file)
    file.close()

    #Skip errors
    if "error" in data.keys():
        continue
    if data["human_players"] != 10:
        continue
    if not data['picks_bans']:
        continue
    # radiant = team 0
    win_team = 0
    if data["radiant_win"]==False:
        win_team=1

    # obtenemos los banned
    picks = pd.DataFrame(data['picks_bans'])
    #if picks.is_pick = 'false' then:
    banned = picks[picks.is_pick==False] #quitamos los picks
    banned = banned.sort_values('order')
    for i in range(14):
        db.append([data['match_id'],banned.iloc[i].hero_id, banned.iloc[i].team == win_team])
    
# Mapeamos el nombre de los héroes con el integer correspondiente
db = pd.DataFrame(db, columns=['Match_id','Hero_id','Win'])
heroes_data=open("hero_stats.json")
hd = json.load(heroes_data)
heroes_data.close()
hd = pd.DataFrame(hd)
s = db.Hero_id.map(hd.set_index('id')['localized_name'])
db['Hero_id'] = s
#Contamos todos las veces que se repite un Hero_id
#Graficamos los Bans
from collections import Counter
letter_counts = Counter(db['Hero_id'])
lc = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
df = pd.DataFrame.from_dict(lc, orient='index')
lf =df.plot(kind='bar')
lf.set_title('Número de Veces Baneado')
plt.show()
#Graficamos el Top10 Heores más baneados de la DPC
ld = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)[0:10])
df = pd.DataFrame.from_dict(ld,orient='index')
lf = df[0:10].plot(kind='bar')
lf.set_title('Top 10 Heroes más Baneados de la DPC SA')
plt.show()


