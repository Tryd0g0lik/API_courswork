import re

from basis import Basis
import requests
import pprint
from datetime import datetime, date, time
import os
import re
import glob
import  shutil


class Ya(Basis):

  def _RevriteNameFile(self, name):
    t = r"^[a-zA-Z0-9]+$.jpg"
    r = re.compile(t, re.S | re.I | re.U)
    for f in glob.glob('*/*.jpg'):
      print(f'glob.glob(): {glob.glob("*/*.jpg")}')
      print(f'f: {f}, name: {name}')
      n = 'files' + '/' + name + '.jpg'
      f = f.replace('\\', '/')
      shutil.move(f, n)
      # name_f =  f.name.replace(f.suffix, '')
      # f.rename(str(f).raplace(name_f, name))

  def _YaFilesSaveInfo(self, album_id, photo_ids):
    # Get_list_foto_album.__init__(self, user_id)

    path = 'files/s'
    mask = '*.jpg'

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

    # d = datetime.date()
    # t = datetime.time()
    # print(f'datetime.date(), datetime.time(): {datetime.now()}')
    name = str(user_likes) + '_' + ((str(str(datetime.now()).replace(' ', '_'))).replace('-', '_')).replace(':', '_')
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



    return data_info
