# Auto Weather Bot 🌦️

O **Auto Weather Bot** é uma aplicação desenvolvida em Python utilizando o framework **FastAPI**. O objetivo do projeto é fornecer alertas climáticos personalizados para uma cidade específica, enviando as informações diretamente para um chat no Telegram. Ele utiliza a **WeatherAPI** para obter os dados meteorológicos e a **API do Telegram** para enviar mensagens.

---

## **Objetivo do Projeto**
O objetivo principal do projeto é:
- Consultar dados climáticos em tempo real para uma cidade específica.
- Formatar as informações meteorológicas de forma clara e amigável.
- Enviar os dados diretamente para um chat no Telegram.

---

## **Como Funciona**
1. O cliente faz uma requisição `POST` para o endpoint `/weather-alert`, informando a cidade e o país no corpo da requisição.
2. O servidor consulta a **WeatherAPI** para obter os dados climáticos da cidade especificada.
3. Os dados são formatados em uma mensagem amigável.
4. A mensagem é enviada para o Telegram utilizando a **API do Telegram**.

---

## **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework para criação de APIs rápidas e eficientes.
- **httpx**: Biblioteca para realizar requisições HTTP assíncronas.
- **WeatherAPI**: API para obter dados climáticos.
- **Telegram Bot API**: API para envio de mensagens ao Telegram.
- **dotenv**: Para gerenciar variáveis de ambiente.

---

## **Pré-requisitos**
1. **Python 3.10+** instalado.
2. Uma conta no [WeatherAPI](https://www.weatherapi.com/) para obter uma chave de API.
3. Um bot configurado no Telegram e o token de acesso gerado pelo [BotFather](https://core.telegram.org/bots#botfather).
4. O ID do chat do Telegram onde as mensagens serão enviadas.

---

## **Configuração**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/auto-weather-bot.git
   cd auto-weather-bot
2. Crie um ambiente virtual
  ''' python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
'''

4. Instale as dependências
'''
pip install -r requirements.txt
'''
