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


  tokens_ = 'vk1.a.GAMpnSpGlrs1YJFfPp5dh6Z_o47g1VCE4yhjh1amdnN3qT7O6TCGWSjcloBhRnjFQhOcGM3LcH0TtIx1pXf77AtTdLkFtBq-GcPc63vE_P5rc54KQPLLPA48BQOXud9k5YIQiW9WJthom0Frieqe-i9i-jZur1b4XQo1PG-Qwz02ldjSaJGDdscW0e3b3Xta'
  api_ = str(5.131)
  r = re.compile(r"^[a-zA-Z0-9]+$", re.S | re.I | re.U)
  print(f'Предоставьте ID пользователя!')
  ID_user = '163911024' #'Tryd0g0lik' #input('ID: ')
  print( "Найден" if r.search(ID_user) else "No")

  autorization_user = Get_autorization_user(ID_user)
  autorization_user.version_api = api_
  autorization_user.access_token = tokens_
  autorization_user.get_authorization()


  list_foto_album = Get_list_foto_album(ID_user)
  list_foto_album.access_token = tokens_
  list_foto_album.version_api = api_
  # list_foto_album.get_list_album()Get_list_foto_album.__init__(user_id)



  list_foto_album.get_photo_selected()

  # list_foto_album.foto_album_selected(list_album)