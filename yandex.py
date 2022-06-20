from basis import Basis
import requests
import pprint
from datetime import datetime

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
    # print(data_)
    return data_

    # if dict_foto == None:
    #   dict_foto = {album_id : [id_foto,size_foto, url_foto]}
    #
    # else:
    #   dict_foto[album_id] += [id_foto,size_foto, url_foto]