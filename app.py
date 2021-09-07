from clases.telegrambot import *
import scrapetube
import re

canal="UCba3hpU7EFBSk817y9qZkiA"
string_referencia="El editorial de Jonatan Viale"
cantidad_videos_referencia=20
contador=0
path_repositorio="your/path/notis_personalizadas/"

tgbot = telegrambot()

videos = scrapetube.get_channel(canal)

tgbot.cargarLlaves(path_repositorio+"keys")

with open(path_repositorio+"id.txt","r") as f:
    id_ult_video=f.readline().replace("\n","")

for video in videos:
    if contador<cantidad_videos_referencia:
        id_=video['videoId']
        if re.search(string_referencia,video["title"]["runs"][0]["text"]) is not None and (id_ult_video !=id_):
            tgbot.notificarRodrigo(id_)
            with open(path_repositorio+"id.txt","w") as f:
                f.write(id_)
        contador+=1
    else :
        break
