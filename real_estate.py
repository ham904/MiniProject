import requests
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as et
import pandas as pd

key = 'Y/DojNPIdumW2rLgBl7+w43rSjNUdCLXFV8DRWdfHGnuvngMBZ+ZZ8WdS3qPc+dcj1AWifo0/C/qforfUB8oEQ=='

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '10', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

response = requests.get(url, params=params)
#print(type(response))
#print(response.text)
# soup = bs(response.text, 'lxml')
# a = soup.find('거래금액')
# print(a)

#%%

import PublicDataReader as pdr
from PublicDataReader import TransactionPrice

service_key = key
api = TransactionPrice(service_key)

# 단일 월 조회
# df = api.get_data(
#     property_type="아파트",
#     trade_type="매매",
#     sigungu_code="11650",
#     year_month="202212",
# )

#%% 수원시 장안구의 시군구 코드 알아내기
code = pdr.code_bdong()
code.head()
code_suwon_bool = code['시군구명'].str.contains('수원시')
code_suwon_df = code[code_suwon_bool]

#%% 기간 내 조회 수원시 장안구

df1 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41111",
    start_year_month="202001",
    end_year_month="202306",
)

#%%
df1 = df1.loc[:,'지역코드':'거래금액']
df1['거래금액'] = df1['거래금액']*10000
df1.to_csv('장안구 아파트 거래.csv', index=False)
#%% 기간 내 조회 수원시 권선구

df2 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41113",
    start_year_month="202001",
    end_year_month="202306",
)
#%%
df2 = df2.loc[:,'지역코드':'거래금액']
df2['거래금액'] = df2['거래금액']*10000
df2.to_csv('권선구 아파트 거래.csv', index=False)

#%% 기간 내 조회 수원시 팔달구

df3 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41115",
    start_year_month="202001",
    end_year_month="202306",
)
#%%
df3 = df3.loc[:,'지역코드':'거래금액']
df3['거래금액'] = df3['거래금액']*10000
df3.to_csv('팔달구 아파트 거래.csv', index=False)
#%% 기간 내 조회 수원시 영통구

df4 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41117",
    start_year_month="202001",
    end_year_month="202306",
)
#%%
df4 = df4.loc[:,'지역코드':'거래금액']
df4['거래금액'] = df4['거래금액']*10000
df4.to_csv('영통구 아파트 거래.csv', index=False)

#%%

region = pd.DataFrame({'지역코드':[41111, 41113, 41115, 41117],
                             '지역구':['장안구', '권선구', '팔달구', '영통구']})
region.to_csv('지역.csv', index=False)

#%% 수원시 아파트거래 value_counts

# temp1 = df1['법정동'].value_counts()
# temp2 = df2['법정동'].value_counts()
# temp3 = df3['법정동'].value_counts()
# temp4 = df4['법정동'].value_counts()
# #%%
# temp5 = pd.concat([temp1,temp2,temp3,temp4])

# temp5.to_csv('지역별거래건수.csv', index=True)

#%% 수원시 아파트 실거래가 상세정보

df5 = pd.concat([df1,df2,df3,df4])
df5.to_csv('수원시 아파트 거래.csv', index=False)
