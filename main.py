from models.genericClient import GenericClient
from models.board import Board
from models.list import List

client = GenericClient("737f990a50b95a1db675188c99175c8a", "ATTA7d15664b7f73521ad1fafa12717b24d6de9136f780224304473d52fe59b0452e0935F6AF", "https://api.trello.com/1")


fetched_board_data = client.get("boards/6645fee8d15bb6bc3076c8e9")
board = Board(fetched_board_data.get("id"),fetched_board_data.get("name"),fetched_board_data.get("desc"),fetched_board_data.get("shortUrl"))
print(board)

fetched_list_data = client.get("lists/66460051007109943d036a44")
trello_list = List(fetched_list_data.get("id"),fetched_list_data.get("name"),fetched_list_data.get("idboard"))
print(trello_list)







#prvi zadatak
# import requests

# api_key = "737f990a50b95a1db675188c99175c8a"
# token = "ATTA7d15664b7f73521ad1fafa12717b24d6de9136f780224304473d52fe59b0452e0935F6AF"
# list_id = "66460051007109943d036a44"
# board_id = "6645fee8d15bb6bc3076c8e9"
# url_post = "https://api.trello.com/1/cards"
# url_get = f'https://api.trello.com/1/boards/{board_id}/cards'

# def ispisi_kartice(url):
#     query = {
#         'key': api_key,
#         'token': token
#     }

#     response = requests.get(url, params=query,timeout=10)

#     if response.status_code == 200:
#         cards = response.json()
#         for card in cards:
#             print(f"Card Name: {card['name']}")
#             print(f"Card ID: {card['id']}")
#             print(f"Card Description: {card['desc']}")
#             print(f"Card URL: {card['shortUrl']}")
#             print("------")
#     else:
#         print(f"Neuspesno: {response.status_code}")
#         print(response.text)

# def napravi_karticu(ime,desc):

#     query_post = {"key":api_key,"token":token,"name":ime,"desc":desc,"idList":list_id}

#     response = requests.post(url_post,query_post,timeout=10)
#     if response.status_code == 200:
#         print("Uspesno napravljena nova kartica!")



# napravi_karticu("TestKartica NOVA","TestDescription NOVA")
# ispisi_kartice(url_get)
