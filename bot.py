import logging
from dotenv import load_dotenv
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters
from handlers import cadastro

# Carregar variáveis do .env
load_dotenv()

# Obter o token do Telegram e o caminho do arquivo JSON do Firebase
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configuração do logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Inicializar o bot com o token
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", cadastro.start)],
        states={
            cadastro.NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, cadastro.get_nome)],
            cadastro.IDADE: [MessageHandler(filters.TEXT & ~filters.COMMAND, cadastro.get_idade)],
            cadastro.CIDADE: [MessageHandler(filters.TEXT & ~filters.COMMAND, cadastro.get_cidade)],
            cadastro.EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, cadastro.get_email)],
            cadastro.INTERESSES: [MessageHandler(filters.TEXT & ~filters.COMMAND, cadastro.get_interesses)],
        },
        fallbacks=[CommandHandler("cancel", cadastro.cancel)],
    )

    app.add_handler(conv_handler)

    # Log de início
    logger.info("Bot iniciado!")
    
    app.run_polling()

if __name__ == "__main__":
    main()
