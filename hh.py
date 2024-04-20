import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

cookies = {
    '_ga': 'GA1.1.1376115409.1713589417',
    '_ga_N909G046PC': 'GS1.1.1713589416.1.1.1713589550.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru',
    # 'cookie': '_ga=GA1.1.1376115409.1713589417; _ga_N909G046PC=GS1.1.1713589416.1.1.1713589550.0.0.0',
    'referer': 'https://new.cooperation.uz/',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'FirstTnvedCategoryId': '2',
    'skip': '0',
    'take': '12',
}

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


response = requests.get(
    'https://new.cooperation.uz/ocelot/api-client/Client/GetAllOffer',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False
)
print(response.json())
