# Hello Classe 4

import json
from twitchAPI.twitch import Twitch

import time #serveix per "adormir" el loop i que no t'expulsi la api 

public = ''
secret  = ''

twitch = Twitch(public, secret)

next = None
loop = 0
def get_str(next, loop):
    resposta = twitch.get_streams(after=next, language="es", first=100)
    print(len(resposta['data']))
    with open(f'{loop}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)

    try:
        next = resposta['pagination']['cursor']
        print('hi ha nova pagina')
        loop = loop + 1
        time.sleep(2) #afegim 2 segons abans de la seguent recaptació
        get_str(next, loop)

    except :
        print('final')
        pass

get_str(next, loop)


