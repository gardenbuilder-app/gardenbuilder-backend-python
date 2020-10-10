import sqlite3
import requests
from decouple import config


def data_pull(pull_type, fruit_type):
    """pull_type- changes the api query type
    token_key feeds in API Tokens
    fruit_type adds elements to pull in data from source"""

    token_key = config('token_key')

    if pull_type == 1:
        url = f'https://trefle.io/api/v1/plants?token={token_key}&q={fruit_type}'
        try:
            r = requests.get(url).json()['data']
            print('Data Pull Completed')
            return r
        except:
            return '404 Error'


def data_loader(ip, plant_type):
    conn = sqlite3.connect('gardenbuilder.sql')
    cur = conn.cursor()
    cmd = 'insert into plant (id,common_name,slug,scientific_name,image_url) values(?,?,?,?,?)'

    try:
        feed_file = data_pull(ip, plant_type)
    except:
        return '404 Error'

    try:
        c = 0
        for i in feed_file:
            tag_id = i['id']
            common_name = i['common_name']
            slug = i['slug']
            scientific_name = i['scientific_name']
            image_url = i['image_url']
            cur.execute(cmd, (tag_id, common_name, slug,
                              scientific_name, image_url))
            conn.commit()
            c += 1
            print('Successfull Inserion: '+str(c))
    except:
        return 'Unique Key Constraint'
    finally:
        conn.close()
    return c

print(data_loader(1,'tomato'))
