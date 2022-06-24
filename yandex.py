import re

from basis import Basis
import requests
import pprint
from datetime import datetime, date, time
import os
import re
import glob
import  shutil
import time

# 163911024

class Ya(Basis):

  def _RevriteNameFile(self):
    t = r"^[a-zA-Z0-9]+$.jpg"
    r = re.compile(t, re.S | re.I | re.U)
    # print('22222: ', glob.glob('*/*.jpg'))
    for f in glob.glob('*/*.jpg'):
      print('33333')
      # print(f'glob.glob(): {glob.glob("*/*.jpg")}')
      print(f'f: {f}')
      # n = 'files' + '/' + name + '.jpg'
      # n = 'files' + '/' + name + '.jpg'

      n = f.replace('\\', '/')
      print(f'n: {n}')
      shutil.move(f, n)
      # name_f =  f.name.replace(f.suffix, '')
      # f.rename(str(f).raplace(name_f, name))

  def _RevriteName(self):
    t = r"^[a-zA-Z0-9]+$.jpg"
    r = re.compile(t, re.S | re.I | re.U)

    for f in glob.glob('*/*.jpg'):
      t = ((str(str(datetime.now()).replace(' ', '_'))).replace('-', '_')).replace(':', '_')
      name = f.split('\\')[-1].split('.')[0]
      n = f.replace('\\' + name, '/' + t)
      print(f'n: {n}')
      shutil.move(f, n)
      time.sleep(1)
      # name_f =  f.name.replace(f.suffix, '')
      # f.rename(str(f).raplace(name_f, name))

  def _CreatFolder(self):
    print('Укажите название папки для корневого каталога Диска')
    name_folder = input('Название: ')


    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    path = 'disk%3A%2F' + name_folder
    params = {'access_token': self.access_token, 'owner_id': self.user_id, 'path' : path}
    requests.put(url=url, params=params)
    return  path

  def _YaFilesSaveInfo(self, album_id, photo_ids):
    path = 'files/s'
    mask = '*.jpg'

    owner_id = self.user_id
    url_album = self.protocol + self.domen + self.path_ + 'photos.get'

    params = {'access_token': self.access_token,  'owner_id': self.user_id, 'album_id': album_id, 'photo_ids': photo_ids,\
              'photo_sizes': 0, 'extended': 1, 'v': self.version_api}


    respons = requests.get(url_album, params=params)

    data_ = respons.json()

    id = data_['response']['items'][0]['id']
    user_likes = data_['response']['items'][0]['likes']['user_likes']

    name = str(user_likes) + '_' + ((str(str(datetime.now()).replace(' ', '_'))).replace('-', '_')).replace(':', '_')

    url = data_['response']['items'][0]['sizes'][-1]['url']
    size = str(data_['response']['items'][0]['sizes'][-1]['height']) + ' ' + 'x' + ' ' +\
           str(data_['response']['items'][0]['sizes'][-1]['width'])

    data_info = {id : {'name' : name, 'size' : size, 'url' : url} }

    check_file = os.path.isfile('files/set_info.txt')
    if check_file == False:
      open('files/set_info.txt', 'x').close()
      txtfile = open('files/set_info.txt', 'a')

    else:
      txtfile = open('files/set_info.txt', 'a')

    txtfile.write(str(data_info))
    txtfile.close()



    return data_info


