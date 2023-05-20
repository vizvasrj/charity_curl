

import requests

cookies = {
    'ak_bmsc': 'BAB35697A5A72564BDAC4775F6E2D8F6~000000000000000000000000000000~YAAQTlvvdT5cgyCIAQAA8y/DNxMSpWuvroNOps7RwTcaakSjkQCr1owr1L+s366eOOdu08WgRMXTnCTUyVpaSGpg2PNrS/z8VQQ/dsdN858B0ShzqEC8IvVHYDjBIkwBtpd16+GKht4fvffyUV04x17WuT6aU5LKurjlpa04Mi5nDz8dTwohk9mfavKgoO01Ye9xmx02nY6WjcM2yrq7hFyvSQGeuxpgzvcfMwss4hSmniQQ0lf1+xntSnVOrLHAiVGyGwRLBw9ktRv57+/IEamPNp0XOHhRfMg6VpkdLccfJHUKOpaWDo3vZQ7F7hhoSUwEVHjhi/vHYMw9upEpCG481MvXcoGSb+agm1Um99toqnteKLTl+ViICzlPA+XYP0DP7neQ1AKEN0nSAmX57db4KtzBBHp5B4Fwv241pDqAxnQLOSfP9J9r6VmYz0dCNw==',
    'bm_sv': '4E9FCDF2103E301D9EC7FE4183F8479A~YAAQTlvvdX1XgyCIAQAA4nrCNxPyTgfylSOmzU2f432MnkxX2V9qIyy08wn9NbV2mr/RiPK6HZurj1r35WuCS7XoJN1FWJam5Mj/mGXJqSBgYQcnDY00BGDsRGmbVfIZG5aic+Yt0N9rlA/Dgko1OIODWi4uSNaaJRjmaheLTXictWif95rC/c2ldfzoWsgg7rwxNE90jFoH08Us7T5KQv4RwWlMnwvOT1Bn2VHcmkYA7Lb9DrwFov0Uv3+mxQYuIvE=~1',
    'bm_mi': 'FEA316D4C354D6F6A5FB0D98A64367FF~YAAQTlvvdRVXgyCIAQAAnGnCNxOLukrFKlu63Gjo0hJYCe6v6/+e6Mu14jICVlQ0MQWRxXimEqojIgDzHwC4NRWKpxv/Zp4cVT1uev2K4ffxv2yP0GBhS8pbOnpk3bLf2pOWZ8NbU6XuJySfQPUWFAaIgypj2GU3KfJkb6xkzdd6PtBn1xKeRpSCHcVGkgL/OduhVz+wHg3BOKWobcS2A1FPK2aZSoaAhMJbDkOgw7SkSAZgKBHq51XarpepEaY6Icx/iPHBct7VGc4GbtXfdsDUyZ+AXP/wDO66q4J2tQrgZDh5bqF5B3jDk6Lsq9cVxCml9sJpKa2c/9cFAxc2~1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.acnc.gov.au/charity/charities',
    # 'Cookie': 'ak_bmsc=BAB35697A5A72564BDAC4775F6E2D8F6~000000000000000000000000000000~YAAQTlvvdT5cgyCIAQAA8y/DNxMSpWuvroNOps7RwTcaakSjkQCr1owr1L+s366eOOdu08WgRMXTnCTUyVpaSGpg2PNrS/z8VQQ/dsdN858B0ShzqEC8IvVHYDjBIkwBtpd16+GKht4fvffyUV04x17WuT6aU5LKurjlpa04Mi5nDz8dTwohk9mfavKgoO01Ye9xmx02nY6WjcM2yrq7hFyvSQGeuxpgzvcfMwss4hSmniQQ0lf1+xntSnVOrLHAiVGyGwRLBw9ktRv57+/IEamPNp0XOHhRfMg6VpkdLccfJHUKOpaWDo3vZQ7F7hhoSUwEVHjhi/vHYMw9upEpCG481MvXcoGSb+agm1Um99toqnteKLTl+ViICzlPA+XYP0DP7neQ1AKEN0nSAmX57db4KtzBBHp5B4Fwv241pDqAxnQLOSfP9J9r6VmYz0dCNw==; bm_sv=4E9FCDF2103E301D9EC7FE4183F8479A~YAAQTlvvdX1XgyCIAQAA4nrCNxPyTgfylSOmzU2f432MnkxX2V9qIyy08wn9NbV2mr/RiPK6HZurj1r35WuCS7XoJN1FWJam5Mj/mGXJqSBgYQcnDY00BGDsRGmbVfIZG5aic+Yt0N9rlA/Dgko1OIODWi4uSNaaJRjmaheLTXictWif95rC/c2ldfzoWsgg7rwxNE90jFoH08Us7T5KQv4RwWlMnwvOT1Bn2VHcmkYA7Lb9DrwFov0Uv3+mxQYuIvE=~1; bm_mi=FEA316D4C354D6F6A5FB0D98A64367FF~YAAQTlvvdRVXgyCIAQAAnGnCNxOLukrFKlu63Gjo0hJYCe6v6/+e6Mu14jICVlQ0MQWRxXimEqojIgDzHwC4NRWKpxv/Zp4cVT1uev2K4ffxv2yP0GBhS8pbOnpk3bLf2pOWZ8NbU6XuJySfQPUWFAaIgypj2GU3KfJkb6xkzdd6PtBn1xKeRpSCHcVGkgL/OduhVz+wHg3BOKWobcS2A1FPK2aZSoaAhMJbDkOgw7SkSAZgKBHq51XarpepEaY6Icx/iPHBct7VGc4GbtXfdsDUyZ+AXP/wDO66q4J2tQrgZDh5bqF5B3jDk6Lsq9cVxCml9sJpKa2c/9cFAxc2~1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

# https://www.acnc.gov.au/charity/charities/161259fc-927a-ed11-81ac-00224893bfad/people

def get_level1(abn: str):
    params = {
        'search': abn,
    }
    response = requests.get('https://www.acnc.gov.au/api/dynamics/search/charity', params=params, cookies=cookies, headers=headers)
    return response.json()



def get_level2(uid: str):
    r = requests.get(f"https://www.acnc.gov.au/api/dynamics/entity/{uid}", cookies=cookies, headers=headers)
    return r.json()


from collections import Counter

# takes json OF UUID data
def get_peoples(data, peoples_array):
    # peoples_array = []
    responsible_persions_ = data.get("data").get("ResponsiblePersons")
    for x in responsible_persions_:
        # print(x.get("Name"))
        peoples_array.append(x.get("Name"))
    return peoples_array

