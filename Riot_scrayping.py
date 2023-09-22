import pandas as pd
import requests
import json
from pandas import json_normalize
from time import sleep

#%% api key 읽어오기
def getAPIkey():
    f = open("./riot_api.txt","r")
    return f.read()
key = getAPIkey()

#%% 챌린저유저의 정보 가져오기

def league_summoner(key, tier,country='kr'):
    request = requests.get(f'https://{country}.api.riotgames.com/tft/league/v1/{tier}?api_key={key}')
    return json.loads(request.content)
ch_summoner = league_summoner(key , tier='challenger')
ch_summoner

#%% 챌린저 유저의 summoner_Id 가져오기

summonerId = []
for sid in ch_summoner['entries']:
    summonerId.append(sid['summonerId'])
summonerId

#%% 서머너 아이디로 해당 유저의 정보 가져오

def summoner_info(summonerId , key, country='kr'):
    request =requests.get(f'https://{country}.api.riotgames.com/tft/summoner/v1/summoners/{summonerId}?api_key={key}')
    return json.loads(request.content)


#%% 서머너 puuid 추출하기

def summoner_puuid(summonerId):
    puuid_list = []
    for i in summonerId:
        si = summoner_info(i,key,'kr')
        puuid_list.append(si['puuid'])
        #puuid_df = pd.DataFrame(puuid_list)
    #return puuid_df
    return puuid_list
puuid = summoner_puuid(summonerId)

#%%

# def get_matchid(puuid, key, n, country='kr'):
#     matchid = []
#     for i in puuid:
#         try:
#             request = requests.get(f'https://{country}.api.riotgames.com/tft/match/v1/matches/by-puuid/{i}/ids?count={n}&api_key={key}')
#             request = json.loads(request.content)
#             matchid.append(request)
#         except:
#             pass
#     return matchid
# ch_matchid = get_matchid(puuid,key,30)
# ch_matchid

#%%

def get_matchid(puuid, key, n, region='asia'):
    matchid = []
    l = 100
    for i in puuid:
        l+=1
        if l%100 == 0:
            sleep(120)
        try:
            request = requests.get(f'https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{i}/ids?count={n}&api_key={key}')
            request = json.loads(request.content)
            matchid.extend(request)
        except:
            pass
    return list(set(matchid))
ch_matchid = get_matchid(puuid,key,20)
ch_matchid

