import requests

# Load API key from external file
try:
    with open(".gitignore", "r") as file:
        chave_api = file.read().strip()
except FileNotFoundError:
    raise FileNotFoundError("O arquivo '.gitignore' não foi encontrado. Certifique-se de que ele existe e contém a chave da API.")

# Define context directly in the code with specific class schedules
prompt = (
    "Você é um assistente virtual que responde como Mussum dos Trapalhões. "
    "O objetivo é informar os horários e aulas da academia fictícia chamada IAFitness. "
    "Responda de forma engraçada e no estilo do Mussum, usando palavras como 'mé', 'cacildis', e 'biritis'. "
    "Aqui estão os horários e aulas da academia IAFitness: "
    "- Musculação: Segunda a sexta, das 6h às 22h. "
    "- Yoga: Sábados, das 8h às 10h. "
    "- Spinning: Terças e quintas, das 19h às 20h. "
    "- Zumba: Quartas e sextas, das 18h às 19h. "
    "- Pilates: Segundas e quartas, das 7h às 8h. "
    "Exemplo de resposta: "
    "'As aulas de musculação acontecem de segunda a sexta, mé. Horário: 6h às 22h, cacildis!' "
    "'As aulas de yoga acontecem aos sábados, mé. Horário: 8h às 10h, cacildis!' "
    "Certifique-se de manter o estilo característico do Mussum em todas as respostas, sempre com humor e criatividade."
)

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {chave_api}",
    "Content-Type": "application/json"
}

def enviar_mensagem_iafitness(mensagem):
    # Always include the system message with the prompt
    Lista_mensagens = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": mensagem}
    ]

    payload = {
        "model": "llama3-8b-8192",  # Pode ser "mixtral-8x7b-32768" ou "gemma-7b-it"
        "messages": Lista_mensagens
    }

    response = requests.post(url, headers=headers, json=payload)
    resposta_json = response.json()

    return resposta_json["choices"][0]["message"]

while True:
    texto = input("Pergunte sobre as aulas da academia IAFitness: ")
    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem_iafitness(texto)
        print("MussumBot:", resposta["content"])
