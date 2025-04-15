import urllib.parse
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from dotenv import load_dotenv
import os

# Configuração
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Location(BaseModel):
    city: str = "Curitiba"
    country: str = "BR"

async def get_weather_data(city: str, country: str) -> dict:
    """Obtém dados com codificação correta e timeout generoso"""
    city_encoded = urllib.parse.quote(city)
    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHERAPI_KEY')}&q={city_encoded},{country}&lang=pt"
    
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
            response = await client.get(url)
            logger.info(f"Resposta da API: {response.status_code}")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro HTTP: {e.response.text}")
        raise HTTPException(502, "Erro na API de clima")
    except Exception as e:
        logger.error(f"Erro de conexão: {str(e)}")
        raise HTTPException(503, "Serviço indisponível")

async def send_telegram_message(text: str) -> bool:
    """Envia com headers explícitos e timeout maior"""
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "chat_id": os.getenv('TELEGRAM_CHAT_ID'),
        "text": text,
        "parse_mode": "HTML"
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=payload, headers=headers)
            logger.info(f"Resposta Telegram: {response.status_code}")
            response.raise_for_status()
            return True
    except Exception as e:
        logger.error(f"Falha no Telegram: {str(e)}")
        return False

@app.post("/weather-alert")
async def weather_alert(location: Location):
    try:
        # Debug: log da requisição recebida
        logger.info(f"Recebido: {location.city}, {location.country}")
        
        # 1. Obter dados
        weather_data = await get_weather_data(location.city, location.country)
        logger.info(f"Dados recebidos: {weather_data}")
        
        # 2. Formatar mensagem
        message = f"""<b>🌦 Previsão para {weather_data['location']['name']}</b>
• 🌡 Temperatura: {weather_data['current']['temp_c']}°C
• ☁ Condição: {weather_data['current']['condition']['text']}"""
        
        # 3. Enviar
        if not await send_telegram_message(message):
            raise HTTPException(500, "Falha ao enviar alerta")
            
        return {"status": "success"}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}", exc_info=True)
        raise HTTPException(500, "Erro interno")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)