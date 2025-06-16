import re
from services.openai_service import generate_reply
from services.sheets_service import salvar_mensagem
from services.ultramsg_service import enviar_mensagem

# Função principal que processa as mensagens recebidas


async def handle_message(data):
    # Extrai a mensagem e o telefone
    mensagem = data.get("message") or data.get("Body") or ""
    telefone = data.get("from") or data.get("From")

    print(f">>> Mensagem recebida: {mensagem}")
    print(f">>> Telefone do remetente: {telefone}")

    # Tenta identificar se há número de senhas solicitadas
    match = re.search(r"(\d+)\s*(senha|senhas)", mensagem.lower())
    quantidade_senhas = int(match.group(1)) if match else None

    # Gera a resposta com a IA
    resposta = await generate_reply(mensagem)

    # Tenta salvar no Google Sheets
    try:
        salvar_mensagem(telefone, mensagem, quantidade_senhas or "")
        print(f"[✅] Dados salvos com quantidade: {quantidade_senhas}")
    except Exception as e:
        print(f"[❌] Erro ao salvar no Google Sheets: {e}")

    # Tenta responder automaticamente no WhatsApp
    try:
        enviar_mensagem(telefone, resposta)
        print(f"[✅] Resposta enviada para {telefone}")
    except Exception as e:
        print(f"[❌] Erro ao enviar resposta via UltraMsg: {e}")

    return resposta
