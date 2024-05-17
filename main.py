import requests
import json

ApiKey="737f990a50b95a1db675188c99175c8a"
Token="ATTA7d15664b7f73521ad1fafa12717b24d6de9136f780224304473d52fe59b0452e0935F6AF"
list_id="66460051007109943d036a44"
board_id="6645fee8d15bb6bc3076c8e9"
urlPost="https://api.trello.com/1/cards"
urlGet=f'https://api.trello.com/1/boards/{board_id}/cards'

query = {
    'key': ApiKey,
    'token': Token
}

response = requests.get(urlGet, params=query)

if response.status_code == 200:

    cards = response.json()

    for card in cards:
        print(f"Card Name: {card['name']}")
        print(f"Card ID: {card['id']}")
        print(f"Card Description: {card['desc']}")
        print(f"Card URL: {card['shortUrl']}")
        print("------")
else:
    print(f"Neuspesno: {response.status_code}")
    print(response.text)


def Napravi_Karticu(ime,desc):

    queryPost = {"key":ApiKey,"token":Token,"name":ime,"desc":desc,"idList":list_id}

    nova_karta = requests.post(urlPost,queryPost)
    print("Uspesno napravljena nova kartica!")



Napravi_Karticu("TestKartica NOVA","TestDescription NOVA")

