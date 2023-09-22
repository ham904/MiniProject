import requests
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as et

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

#%% 기간 내 조회 수원시 장안구

df1 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41111",
    start_year_month="202301",
    end_year_month="202306",
)
df1.to_csv('장안구 아파트 거래.csv', index=False)
#%% 기간 내 조회 수원시 권선구

df2 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41113",
    start_year_month="202301",
    end_year_month="202306",
)
#%% 기간 내 조회 수원시 팔달구

df3 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41115",
    start_year_month="202301",
    end_year_month="202306",
)
#%% 기간 내 조회 수원시 영통구

df4 = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41117",
    start_year_month="202301",
    end_year_month="202306",
)

#%% 화성시
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41590",
    start_year_month="202301",
    end_year_month="202306",
)

#%% 수원시 장안구의 시군구 코드 알아내기
code = pdr.code_bdong()
code.head()
code_suwon_bool = code['시군구명'].str.contains('수원시')
code_suwon_df = code[code_suwon_bool]

#%%
code_hwasung_bool = code['시군구명'].str.contains('화성시')
code_hwasung_df = code[code_hwasung_bool]

#%% 금융산업?

url = 'http://apis.data.go.kr/1160100/service/GetFnCoBasiInfoService/getFnCoOutl'
params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '10', 'resultType' : 'xml', 'basDt' : '20200408', 'crno' : '1101113892240', 'fncoNm' : '메리츠자산운용' }

response = requests.get(url, params=params)
print(response.text)