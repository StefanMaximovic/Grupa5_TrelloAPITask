from genericClient import GenericClient
from models.board import Board
from models.list import List
from models.card import Card
from models.checkList import CheckList
from models.comment import Comment
from fileManager import FileManager

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from databaseConnection import DatabaseConnection
import trelloModels
from trelloModels import Board as BoardTrello
from trelloModels import List as ListaTrello
from trelloModels import Card as CardTrello
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///trello.db')


Session = sessionmaker(bind=engine)

session = Session()

# board1 = BoardTrello(id="6645fee8d15bb6bc3076c8e9a", name="Board 1")

# session.add(board1)
# session.commit()


client = GenericClient("737f990a50b95a1db675188c99175c8a", "ATTA7d15664b7f73521ad1fafa12717b24d6de9136f780224304473d52fe59b0452e0935F6AF", "https://api.trello.com/1")
file_manager = FileManager('.')


try:
    fetched_board_data = client.get("boards/6645fee8d15bb6bc3076c8e9")
    # board = Board(
    #     fetched_board_data.get("id"),
    #     fetched_board_data.get("name"),
    #     fetched_board_data.get("desc"),
    #     fetched_board_data.get("shortUrl")
    # )
    board1 = BoardTrello(id=fetched_board_data.get("id"),name=fetched_board_data.get("name"))
   # print(board)
    session.add(board1)
    session.commit()
    print("------")
except Exception as e:
    print(f"An error occurred: {e}")

#file_manager.save_to_file('board.json', board.__dict__)

try:
    fetched_list_data = client.get("lists/66460051007109943d036a44")
    #trello_list = List(list_id, list_name, list_idboard)
    lista1 = ListaTrello(id=fetched_list_data.get("id"), name=fetched_list_data.get("name"), board_id=fetched_list_data.get("66460051007109943d036a44"))
    #print(trello_list)
    session.add(lista1)
    session.commit()
    print("------")
except AttributeError as e:
    print(f"Attribute error: {e}")
except KeyError as e:
    print(f"Key error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#file_manager.save_to_file('lists.json', trello_list.__dict__)

cards = []
checklists = []
comments = []
fetched_card_data = client.get("boards/6645fee8d15bb6bc3076c8e9/cards")
for card in fetched_card_data:
    session.add(CardTrello(id=card.get("id"),title=card.get("name"),description=card.get("desc"),list_id="66460051007109943d036a44"))
    session.commit()
    #cards.append(Card(card.get("id"), card.get("name"), card.get("desc"), card.get("shortUrl")))

#Fetch checklist for each card
cards = []
checklists = []
comments = []

try:
    fetched_card_data = client.get("boards/6645fee8d15bb6bc3076c8e9/cards")
    for card in fetched_card_data:
        try:
            cards.append(Card(card.get("id"), card.get("name"), card.get("desc"), card.get("shortUrl")))
            card_checklist_data = client.get(f'cards/{card.get("id")}/checklists')
            for checklist_data in card_checklist_data:
                try:
                    checklists.append(CheckList(
                        checklist_data.get("id"),
                        checklist_data.get("name"),
                        checklist_data.get("idBoard"),
                        checklist_data.get("idCard")
                    ))
                except Exception as e:
                    print(f"Error while processing checklist data: {e}")
        except Exception as e:
            print(f"Error while processing card data: {e}")

except Exception as e:
    print(f"Error while fetching card data: {e}")


#Fetch comments for each card
try:
    card_comments_data = client.get(f'cards/{card.get("id")}/actions?filter=commentCard')
    for attachment_data in card_comments_data:
        comment = Comment(
            attachment_data.get("id"),
            attachment_data.get("idMemberCreator"),
            attachment_data.get("date"),
            attachment_data['data']['text']
        )
        comments.append(comment)
except Exception as e:
    print(f"Error occurred while fetching card data: {e}")

#Fetch attachment for each card
try:
    card_attachments = client.get(f'cards/{card.get("id")}/attachments')
    for attachment in card_attachments:
        attachment_data = client.get_attachment(attachment.get('url'))
        img_name = attachment.get('name')
        img_id = attachment.get('id')
        file_manager.save_attachment(f"{img_name.replace('.png', '')}-{img_id}.png", attachment_data.content)
except Exception as e:
    print(f"Error occurred while fetching card data: {e}")

print("Cards:")
for card in cards:
    print(card)
    print("------")

print("\nChecklists:")
for check_list in checklists:
    print(check_list)
    print("------")

print("\nComments:")
for comment in comments:
    print(comment)
    print("------")

file_manager.save_to_file('cards.json', [card.__dict__ for card in cards])

file_manager.save_to_file('checklists.json', [check_list.__dict__ for check_list in checklists])

file_manager.save_to_file('comments.json', [comment.__dict__ for comment in comments])


print("Files:")
file_manager.list_files()

print("\nBoard:")
file_manager.display_file_content('board.json')

print("\nList:")
file_manager.display_file_content('lists.json')

print("\nCards:")
file_manager.display_file_content('cards.json')

print("\nChecklist:")
file_manager.display_file_content('checklists.json')

print("\nComments:")
file_manager.display_file_content('comments.json')

print("\nAttachments:")
file_manager.display_attachments()



#Prvi zadatak
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
