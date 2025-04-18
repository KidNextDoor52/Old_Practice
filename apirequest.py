import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'



def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []

    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(['episode']),             
        }

        charlist.append(char)

    return charlist


    #name = data['results'][0]['name']
    #episodes = data['results'][0]['episode']

mainlist = []

data = main_request(baseurl,  endpoint, 2)
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))
#print(parse_json(data))

#print(len(mainlist))

page_df = pd.DataFrame(mainlist)

page_df.to_csv('charlist.csv', index=False)
#print(page_df.head, page_df.tail)



