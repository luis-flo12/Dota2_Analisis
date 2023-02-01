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

    # obtenemos los picks
    picks = pd.DataFrame(data['picks_bans'])
    picks = picks[picks.is_pick] #quitamos los bans
    picks = picks.sort_values('order') #sort by order
    #radiant_team = data['radiant_team']['name']
    #dire_team = data['dire_team']['name']
    for i in range(10):
        db.append([data['match_id'],picks.iloc[i].hero_id, picks.iloc[i].team == win_team])
db = pd.DataFrame(db, columns=['Match_id','Hero_id','Win'])
    #db.Team_name=db.Team_name.map({1:radiant_team, 0:dire_team})

heroes_data=open("hero_stats.json")
hd = json.load(heroes_data)
heroes_data.close()
hd = pd.DataFrame(hd)
s = db.Hero_id.map(hd.set_index('id')['localized_name'])
db['Hero_id'] = s
print(db)
#Contamos todos las veces que se repite un Hero_id
from collections import Counter
letter_counts = Counter(db['Hero_id'])
lc = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
df = pd.DataFrame.from_dict(lc, orient='index')
lf =df.plot(kind='bar')
lf.set_title('Número de veces pickeado')
plt.show()

#Graficamos los Top10 Heroes más Pickeados esta DPC SA
ld = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)[0:10])
df = pd.DataFrame.from_dict(ld,orient='index')
lf = df[0:10].plot(kind='bar')
lf.set_title('Top 10 Heroes más Pickeados de la DPC SA')
plt.show()



#calculamos el winrate
#solo tomamos en cuenta los heroes que han tenido más de 10 partidas
wr = db.Hero_id.value_counts()
keep = wr[wr >=10].index
ls = db[db.Hero_id.isin(keep)]

#Graficamos el Winrate de los heroes que han sido escogidos más de 10 veces Durante la DPC SA
winrate = ls.groupby('Hero_id')['Win'].mean()
winrate = winrate.sort_values(ascending=False)
figure = winrate.plot(kind='bar')
figure.set_ylabel('Win Rate')
figure.set_title('Winrate de Heroes que han sido escogidos más de 10 veces')
plt.show()

#Graficamos el Winrate de los Top 10 heroes que han sido escogidos más de 10 veces Durante la DPC SA
figure = winrate[0:10].plot(kind='bar')
figure.set_ylabel('Win Rate')
figure.set_title('Top 10 Heroes con el Winrate más alto')
plt.show()