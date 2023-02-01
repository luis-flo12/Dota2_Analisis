from bs4 import BeautifulSoup as BS
import requests, json, time, os
url = ["https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&series_status=live_or_completed" , "https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&page=2&series_status=live_or_completed", "https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&page=3&series_status=live_or_completed","https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&page=4&series_status=live_or_completed"]
headers = {
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}
matches_id = []
for i in url:
    r=requests.get(i, headers=headers)
    soup = BS(r.text,'lxml')
    for x in soup.select('article a[href*="/matches/"]'):
        matches_id.append(x.text)
#print(matches_id)
for u in matches_id:
    data = requests.get("https://api.opendota.com/api/matches/"+ u)
    #print("Get:",u)
    partidas= data.json()
    #Guardamos la data
    file = open(u + '_partidas.json','x')
    json.dump(partidas,file)
    file.close()

