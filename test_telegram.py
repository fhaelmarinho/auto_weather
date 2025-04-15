from main import send_telegram_message  # Importa a função do arquivo main.py

if __name__ == "__main__":
    import asyncio
    asyncio.run(send_telegram_message(message))