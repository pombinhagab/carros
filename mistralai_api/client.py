from mistralai import Mistral
from decouple import config

api_key = config('MISTRAL_KEY')
print("API Key =", api_key)
model = "mistral-small-latest"

def get_car_ai_bio(modelCar, brandCar, factoryYear):
    client = Mistral(api_key=api_key)
    prompt = f"""
Crie uma descrição de venda com no máximo 250 caracteres para o carro {brandCar} {modelCar} {factoryYear}.
A descrição deve ser realista e fluida, sem usar placeholders ou chaves.
Destaque pontos comuns desse modelo, como motor, conforto, tecnologia e design.
Não mencione a contagem de caractéres no final da mensagem.
Por favor não coloque caracteres especiais como aspas ou backticks no início ou fim da mensagem.
"""
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.7,
    )
    return chat_response.choices[0].message.content