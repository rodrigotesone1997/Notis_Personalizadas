import json # Paquete que permite manipular archivos .dat y .json
import requests # Paquete para hacer requests

class telegrambot:

    def cargarLlaves(self,name):
        
        # Leer el .dat
        
        retorno = False
        try:
            with open(name + ".dat", "r") as f:
                loaded_keys = json.loads(f.read())
            self.token_telegram=loaded_keys["token_telegram"] # Acceso al bot
            self.id_Rodrigo=loaded_keys["id_Rodrigo"] # Rodrigo
            retorno = True
        except:
            pass
        return retorno

    def notificarRodrigo(self,id_video):
        url=f"https://www.youtube.com/watch?v={id_video}"
        mensaje =f"Joni Viale publico una nueva editorial:\n\n[link]({url})"
        texto="https://api.telegram.org/bot"+self.token_telegram+"/sendMessage?chat_id="+self.id_Rodrigo+"&parse_mode=MarkdownV2&text="+mensaje
        
        response=requests.get(texto)
        
        return response.json()