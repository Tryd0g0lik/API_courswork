from basis import Basis
import os.path
import re
from pprint import pprint
import requests

class Get_Token(Basis):

  def get_user_token(self):

    # print('ghbdtn')
    check_token = os.path.isfile('files/token.txt')
    print('Наличие файла: ', check_token)
    if check_token == False:
      open('files/token.txt', 'x').close()
      print("В папке 'files' файл 'token.txt' - разместите в нем свой токен")
      with open('files/token.txt', 'w', encoding='utf-8') as open_file:


        token_text = (input("Введите ТОКЕН-ключ: ")).strip()

        if token_text != None:
          open_file.write(token_text)
          open_file.close()

    else:
      file_size = os.path.getsize('files/token.txt')
      print('Вес файла: ', file_size)
      if file_size > 0:
        with open('files/token.txt', 'r', encoding='utf-8') as open_file:
          self.token = open_file.read()
          return self.token

      elif file_size == 0:
        with open('files/token.txt', 'w', encoding='utf-8') as open_file:
          print("В папке 'files' файл 'token.txt' - разместите в нем свой токен")
          token_text = (input("Введите ТОКЕН-ключ: ")).strip()
          if token_text != None:
            open_file.write(token_text)
            self.token = open_file.read()
            return self.token

class Get_autorization_user(Basis):
  def __init__(self, user_id):

    self.user_id = user_id
    self.title_method = 'users.get'
    self.version_api = None
    self.access_token = None

  def get_authorization(self):
    super().__init__()
    self.params = {'user_ids': self.user_id, 'access_token': self.access_token, 'fields': 'has_photo, maiden_name, '\
      'screen_name, photo_400_orig', 'v': self.version_api}
    # print(f"user_ids: {self.user_id}, access_token': {self.access_token}, fields: 'has_photo, maiden_name, "
    #       f"screen_name, "
    #  f"photo_400_orig, v: {self.version_api}")
    url = self.protocol + self.domen + self.path_ + self.title_method
    print( ' url', url)
    r = re.compile(r"^[a-zA-Z0-9]+$", re.S | re.I | re.U)

    if r.search(str(self.user_id)):
      informasion = requests.get(url, params=self.params)

      if informasion.status_code >= 300:
        print(f"Что-то пошло не так. Ответ: {informasion.status_code}")

      elif informasion.status_code < 300:
          print(f"informasion.status_code: {informasion.status_code}")
          edict_informasion = informasion.json()
          print(edict_informasion)
          print(f"Имя: {edict_informasion['response'][0]['first_name']}")
          print(f" ")
          print(f"Фамилия: {edict_informasion['response'][0]['last_name']}")
          print(f" ")
          print(f"Имя в социальной сети: {edict_informasion['response'][0]['screen_name']}")
          print(f" ")
          print(f"id: {edict_informasion['response'][0]['id']}")

class Get_list_foto_album(Get_autorization_user):
  def __init__(self, user_id):
    super().__init__(user_id)
    Basis.__init__(self)
    self.user_id = user_id
    # self.title_method = 'account.getInfo'
    self.title_method = 'photos.getAlbums'
    self.album_ids  = None
    self.version_api  = None
    self.access_token  = None




  def _get_list_album(self):
    # Basis.__init__(self)
    lsit_id_albums = []



    url = self.protocol + self.domen + self.path_ + self.title_method

    self.params = {'user_ids': self.user_id, 'access_token': self.access_token, 'fields': 'bdate', \
                   'v': self.version_api, 'album_ids': self.album_ids, 'offset': 0}
    r = re.compile(r"^[a-zA-Z0-9]+$", re.S | re.I | re.U)
    informasion = requests.get(url, params = self.params)


    if r.search(str(self.user_id)):
      if informasion.status_code >= 300:
        print(f"Что-то, с альбомами пошло не так. Ответ: {informasion.status_code}")


      elif informasion.status_code < 300:
        edict_informasion = informasion.json()
        # print(informasion.status_code)
        print(f"Колличество найденных альбомов:{edict_informasion['response']['count']}")
        for i in range(len(edict_informasion['response']['items'])):


          print(f"ID-альбома:{edict_informasion['response']['items'][i]['id']}")
          print(f"Заголовок альбома:{edict_informasion['response']['items'][i]['title']}")
          # print(f"Id-обложки (фото превью):{edict_informasion['response']['items'][i]['thumb_id']}")
          print(f"Количество фотографий в альбоме:{edict_informasion['response']['items'][i]['size']}")
          print(" ")
          lsit_id_albums.append(str(edict_informasion['response']['items'][i]['id']))

        print('22', lsit_id_albums)
        return lsit_id_albums

  # def _images_of_alboum(self, user_id):
  #   self.user_id = Get_list_foto_album.__init__(self, user_id)
  #   self.title_method = 'photos.get'
  #   lsit_id_albums = Get_list_foto_album._get_list_album(self)
  #   # Get_list_foto_album.__init__(user_id)
  #
  #   params = {'owner_id' : self.user_id, 'album_id' : lsit_id_albums,\
  #             'count' : edict_informasion['response']['items'][i]['size'] }
  #   # params = {}
  #   url = self.protocol + self.domen + self.path_ + self.title_method
  #   photo_ = requests.get(url, params = params)
  #   print(photo_)

  def index_album_selected(self):

    lsit_id_albums = Get_list_foto_album._get_list_album(self)
    print('Перечислите "ID-альбомов" которые желаете посмотреть для созранения фотографий ')
    selected_album = (input("Вставьте через запятую с пробелом ', ': ")).strip(' ') \
      .split(', ')

    index_i = []
    for i in selected_album:
      index_i.append(lsit_id_albums.index(int(str(i).strip("][").strip("'").strip(" "))))

    print('index_i: ', index_i)
    # _images_of_alboum(self, user_id)

