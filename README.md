# IA Chatbot Fitness - MussumBot

## Descrição

O **IA Chatbot Fitness** é um assistente virtual que responde no estilo humorístico do Mussum dos Trapalhões. Ele foi projetado para fornecer informações sobre os horários e aulas da academia fictícia chamada **IAFitness**. As respostas são engraçadas e criativas, utilizando expressões características como "mé", "cacildis" e "biritis".

## Funcionalidades

- Responde perguntas sobre os horários e aulas da academia IAFitness.
- Gera respostas no estilo do Mussum, com humor e criatividade.
- Suporte para comandos de saída ao digitar "sair".

## Horários e Aulas da Academia IAFitness

- **Musculação**: Segunda a sexta, das 6h às 22h.
- **Yoga**: Sábados, das 8h às 10h.
- **Spinning**: Terças e quintas, das 19h às 20h.
- **Zumba**: Quartas e sextas, das 18h às 19h.
- **Pilates**: Segundas e quartas, das 7h às 8h.

## Exemplo de Resposta

```
Usuário: Quais são os horários de yoga?
MussumBot: As aulas de yoga acontecem aos sábados, mé. Horário: 8h às 10h, cacildis!
```

## Requisitos

- Python 3.7 ou superior
- Biblioteca `requests`
- Arquivo `api_key.txt` contendo a chave da API

## Configuração

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Instale as dependências:
   ```bash
   pip install requests
   ```

3. Crie um arquivo `api_key.txt` no mesmo diretório do código e insira sua chave da API.

4. Execute o chatbot:
   ```bash
   python ChatBot_IAFitness.py
   ```

## Uso

- Execute o script e faça perguntas sobre os horários e aulas da academia.
- Para sair, digite "sair".

## Observações

Este projeto utiliza uma API de IA para gerar respostas. Certifique-se de que sua chave da API está ativa e válida.

## Licença

Este projeto é apenas para fins educacionais e não possui uma licença específica.
