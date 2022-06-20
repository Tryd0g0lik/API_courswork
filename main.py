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

  # print('Строка для авторизации приложения - получить токен')
  # https://oauth.vk.com/authorize?client_id=8183873&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.131

  import requests


  # print('''Разместите токен в "tokens_".''')
  tokens = Get_Token()
  tokens_ = tokens.get_user_token()
  # tokens_ = 'vk1.a. ТОКЕН tB0U4IiL1LHLkkGkih7Ku8i3L ТОКЕН dw15H ТОКЕН NpQL1tE-LFI7kOz_ ТОКЕН qGJqPOG7uW7Yczhj' \
  #           '-wc8MxZlgXpFLucoe ТОКЕН wE6O69CV_c4Lp18jHI ТОКЕН RGvOWh8Asd1oGNG-lG9_'

  api_ = str(5.131)
  r = re.compile(r"^[a-zA-Z0-9]+$", re.S | re.I | re.U)
  print(f'Предоставьте ID пользователя!')
  ID_user = input('ID: ')
  print( "Найден" if r.search(ID_user) else "No")

  autorization_user = Get_autorization_user(ID_user)
  autorization_user.version_api = api_
  autorization_user.access_token = tokens_
  autorization_user.get_authorization()


  list_foto_album = Get_list_foto_album(ID_user)
  # list_foto_album.album_ids = 258774378
  list_foto_album.access_token = tokens_
  list_foto_album.version_api = api_





  list_foto_album.get_photo_selected()
  print('Сделано!')

