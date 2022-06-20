from basis import Basis
import requests
import pprint
from datetime import datetime
import os
import csv

class Ya(Basis):

  def _YaFilesSaveInfo(self, album_id, photo_ids):
    # Get_list_foto_album.__init__(self, user_id)
    # photo_ids = None
    url_foto = None
    dict_foto = None

    owner_id = self.user_id
    url_album = self.protocol + self.domen + self.path_ + 'photos.get'
    print(f'url_album: {url_album}')

    params = {'access_token': self.access_token,  'owner_id': self.user_id, 'album_id': album_id, 'photo_ids': photo_ids,\
              'photo_sizes': 0, 'extended': 1, 'v': self.version_api}
    # params = {'owner_id': self.user_id, 'album_id': album_id, 'photo_ids': photo_ids, 'rev': 0, \
    #           'photo_sizes': 0, 'extended': 1, 'v': self.version_api}

    print(f'params: {params}')
    respons = requests.get(url_album, params=params)

    print(f'respons: {respons}')
    data_ = respons.json()

    print(f'data_: {data_}')


    id = data_['response']['items'][0]['id']
    user_likes = data_['response']['items'][0]['likes']['user_likes']
    print(f'user_likes : {user_likes }')

    name = str(user_likes) + '_' + str(datetime.today())
    # print(f"data_['response']['items'][0]['size']: {data_['response']['items'][0]['sizes']}")
    url = data_['response']['items'][0]['sizes'][-1]['url']
    size = str(data_['response']['items'][0]['sizes'][-1]['height']) + ' ' + 'x' + ' ' +\
           str(data_['response']['items'][0]['sizes'][-1]['width'])

    data_info = {id : {'name' : name, 'size' : size, 'url' : url} }
    print(f'data_info: {data_info}')

    check_file = os.path.isfile('files/set_info.txt')
    if check_file == False:
      open('files/set_info.txt', 'x').close()
      txtfile = open('files/set_info.txt', 'a')

    else:
      txtfile = open('files/set_info.txt', 'a')

    txtfile.write(str(data_info))
    txtfile.close()

    return data_
