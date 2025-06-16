from fastapi import FastAPI, Request
from handlers.message_handler import handle_message

app = FastAPI()

# Rota principal que recebe as mensagens do WhatsApp (ou testes locais)


@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    body = await request.json()
    print(">>> Requisição recebida no /webhook:", body)

    response = await handle_message(body)
    return {"response": response}
