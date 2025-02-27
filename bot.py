import time
import requests

TOKEN = 7720182921:AAERle2h8iUv_u5ToriU_VqWoDMqTK5lQtE
CHAT_ID = 1122002906
MENSAGEM = "Atualização do projeto: O desenvolvimento está em andamento."

def enviar_mensagem():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": MENSAGEM}
    requests.post(url, data=data)


while True:
    enviar_mensagem()
    time.sleep(3600)
