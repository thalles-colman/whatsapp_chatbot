import asyncio
from handlers.message_handler import handle_message


async def testar_handler():
    dados_teste = {
        "from": "+5581996792099",
        "message": "Quero 3 senhas para o evento"
    }

    print(">>> Enviando dados de teste para handle_message()...")
    resposta = await handle_message(dados_teste)
    print(">>> Resposta final retornada pela IA:")
    print(resposta)

asyncio.run(testar_handler())
