# openai_service.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_reply(prompt: str) -> str:
    print(">>> Entrou em generate_reply()")
    print(f">>> Prompt recebido: {prompt}")

    try:
        print(">>> Chamando a API da OpenAI")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um atendente educado e prestativo."},
                {"role": "user", "content": prompt}
            ]
        )

        print(">>> Resposta recebida da OpenAI:", response)
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        print("[ERRO OPENAI]", type(e).__name__, ":", e)  # Mostra tipo e mensagem
        return "Desculpe, houve um erro ao processar sua solicitação."
