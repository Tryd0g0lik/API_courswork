from basis import Basis
import os
import re
from pprint import pprint
import requests



class Get_Token(Basis):

  def get_user_token(self):

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

    self.title_method = 'photos.getAlbums'
    self.album_ids  = None
    self.version_api  = None
    self.access_token  = None





  def _get_list_album(self):

    lsit_id_albums = []



    url = self.protocol + self.domen + self.path_ + self.title_method

    self.params = {'owner_id': self.user_id, 'access_token': self.access_token, 'fields': 'bdate', \
                   'v': self.version_api, 'album_ids': self.album_ids, 'offset': 0}
    r_ = re.compile(r"^[a-zA-Z0-9]+$", re.S | re.I | re.U)
    informasion = requests.get(url, params = self.params)


    if r_.search(str(self.user_id)):
      if informasion.status_code >= 300:
        print(f"Что-то, с альбомами пошло не так. Ответ: {informasion.status_code}")


      elif informasion.status_code < 300:
        edict_informasion = informasion.json()

        print(f"Колличество найденных альбомов:{edict_informasion['response']['count']}")
        for i in range(len(edict_informasion['response']['items'])):


          print(f"ID-альбома:{edict_informasion['response']['items'][i]['id']}")
          print(f"Заголовок альбома:{edict_informasion['response']['items'][i]['title']}")

          print(f"Количество фотографий в альбоме:{edict_informasion['response']['items'][i]['size']}")
          print(" ")
          lsit_id_albums.append(str(edict_informasion['response']['items'][i]['id']))


        return lsit_id_albums

  def _images_of_alboum(self, selected_album):

    self.title_method = 'photos.get'
    photo_ = {}
    for id_albums in selected_album:
      id_albums = id_albums.strip(',').strip("][").strip('"').strip("'").strip('"').strip(" ").strip(',')

      params = {'access_token': self.access_token,  'owner_id' : self.user_id, 'album_id' : 'saved', 'rev' : 0,\
                'album_id' : str(id_albums), 'extended' : 0, 'photo_sizes'  : 0, 'v' : self.version_api }

      url = self.protocol + self.domen + self.path_ + self.title_method

      if photo_ == {}:
        response = requests.get(url, params = params)

        photo_['photo_'] = [response.json()]
      else:
        response = requests.get(url, params = params)

        photo_['photo_'].append(response.json())




    return photo_

  def _index_album_selected(self):

    lsit_id_albums = Get_list_foto_album._get_list_album(self)
    print('Перечислите "ID-альбомов" которые желаете посмотреть для созранения фотографий ')
    selected_album = (input("Вставьте через запятую с пробелом ', ': ")).strip(' ') \
      .split(', ')

    index_i = []
    list_photo_dict = {}

    for i in selected_album:

      index_i.append(lsit_id_albums.index(str(i).strip(',').strip("][").strip('"').strip("'").strip('"').strip(" ").strip(',')))


    photo_ = Get_list_foto_album._images_of_alboum(self, selected_album)

    for one_dict in photo_['photo_']:

      for size_defoult in one_dict['response']['items']:

        print(f"Id альбома: {size_defoult['album_id']}")
        print(f"Фотография id: {size_defoult['id']}")

        size_id = len(size_defoult['sizes'])-1

        print(f"Фотография высота: {size_defoult['sizes'][ size_id]['height']} x ширина: "
              f" {size_defoult['sizes'][ size_id]['width']}")
        print(f"Фотография URL: {size_defoult['sizes'][ size_id]['url']}")
        print(' ')

        if list_photo_dict == {}:
          list_photo_dict['max_photo_size'] = [{'id_allboum' : size_defoult['album_id'], 'url' :\
            size_defoult['sizes'][size_id]['url']}]

        else:
          list_photo_dict['max_photo_size'].append({'id_allboum' : size_defoult['album_id'], 'url' :\
            size_defoult['sizes'][ size_id]['url']})

    return list_photo_dict

  def _Ya_disk_upload(self, href, file):

    t = requests.put(href, data=open('files/' + file, 'rb'))


  def _Ya_disk_get_link(self):
    files = os.listdir('files/')
    request_ = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    Authorization = "OAuth {}".format('AQAAAAAEHsPoAADLW4SZ-XnrG0fgq7H0CmynvHw')
    header = {'Content-Type': 'application/json', 'Authorization': Authorization}

    template = r"\S+\.[jpg][png][gif]"
    r = re.compile(template)

    for f in files:

      res = None
      if r.search(f):

        path = "D%3A%2Fdjango-sites%2FNetologe%2Fcoursework-vk%2Ffiles%2F" + f
        params = {'path': path, 'overwrite': 'true'}

        respons = requests.get(request_, headers=header, params = params)

        res = respons.json()
        href = res['href']


        Get_list_foto_album._Ya_disk_upload(self, href, f)


  def get_photo_selected(self):
    get_photo_list = Get_list_foto_album._index_album_selected(self)

    self.title_method = 'photos.getUploadServer'
    url = self.protocol + self.domen + self.path_ + self.title_method

    print("Сохраняем фотографии")
    print('''Вначале сохраним в "...\coursework-vk\files"''')
    print('После закачиваем на Яндекс Диск')
    id_before = 0

    for list_photo in get_photo_list['max_photo_size']:
      picturies = str(list_photo['url']).split("/")[-1].split("?")[0]

      # Download a photo from the web
      link_ = "files/" + picturies

      p = requests.get(list_photo['url'])

      out = open(link_, "wb")

      out.write(p.content)
      out.close()



      Get_list_foto_album._Ya_disk_get_link(self)



