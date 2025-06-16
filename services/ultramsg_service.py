import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Variáveis de ambiente
INSTANCE_ID = os.getenv("ULTRAMSG_INSTANCE_ID")
TOKEN = os.getenv("ULTRAMSG_TOKEN")
BASE_URL = os.getenv("ULTRAMSG_API_URL")

# Corrigido: Token como parâmetro GET na URL
URL = f"{BASE_URL}/{INSTANCE_ID}/messages/chat?token={TOKEN}"



def enviar_mensagem(numero: str, mensagem: str):

    payload = {
        "to": numero,
        "body": mensagem,
        "priority": 10
    }

    try:
        resposta = requests.post(URL, data=payload)
        print("[UltraMsg] Resposta:", resposta.text)
    except Exception as e:
        print("[ERRO UltraMsg]", e)
