# Users
#   Методы для работы с данными пользователей.

# account.getInfo
#     Возвращает информацию о текущем аккаунте

# account.lookupContacts
#   Позволяет искать пользователей ВКонтакте,

#   account.setOffline
#     Помечает текущего пользователя как offline

#   account.setOnline
#     Помечает текущего пользователя как online

# Photos
#   Методы для работы с фотографиями.

# Search
#   Методы для работы с поиском.
#
# Stats
#   Методы для работы со статистикой.
#
# Status
#   Методы для работы со статусом.

#   get
#     Возвращает список фотографий в альбоме
#
#   getTags
#     Возвращает список отметок на фотографии.

# 1. Спросить сколько фотографий загружать (по умолчанию 5)?
# 2. Загружать последний 5 фото

# token = '6ac0159505b8984221'
if __name__ == '__main__':
  from get import Get_Token, Get_autorization_user, Get_list_foto_album
  import re

  # token_ = 'vk1.a.TgR9u-XAbHLI84sT1oyEG_v0nsux2LRU0duiZdGpg9i89bstFtmIRVZoxm4vKE7OhlN-_sDJgrKFRNuohogSPKms6sT1IpvsyYFimHbnRo1PompF4HSsp4ZTlV6ctdqo6O8tVtPg6qDcxMfO41k9_OZCBUxMV8cTl4dpXyLQRxieLM_eV7qaI94DqhLBEMEJ'
  # token_ = '7de41821c52ae0f2bd95f4d6e25c004a17ca92a01979ccf4d72d0ba209d13e1dc77a36da2adaf12e56ab5'
  token_ = 'vk1.a.TgR9u-XAbHLI84sT1oyEG_v0nsux2LRU0duiZdGpg9i89bstFtmIRVZoxm4vKE7OhlN-_sDJgrKFRNuohogSPKms6sT1IpvsyYFimHbnRo1PompF4HSsp4ZTlV6ctdqo6O8tVtPg6qDcxMfO41k9_OZCBUxMV8cTl4dpXyLQRxieLM_eV7qaI94DqhLBEMEJ'
  api_ = str(5.131)
  r = re.compile(r"^[a-zA-Z0-9]+$", re.S | re.I | re.U)
  print(f'Предоставьте ID пользователя!')
  ID_user = '163911024' #'Tryd0g0lik' #input('ID: ')
  print( "Найден" if r.search(ID_user) else "No")

  autorization_user = Get_autorization_user(ID_user)
  autorization_user.version_api = api_
  autorization_user.access_token = token_
  autorization_user.get_authorization()


  list_foto_album = Get_list_foto_album(ID_user)
  list_foto_album.access_token = token_
  list_foto_album.version_api = api_
  # list_foto_album.get_list_album()Get_list_foto_album.__init__(user_id)



  list_foto_album.get_photo_selected()

  # list_foto_album.foto_album_selected(list_album)