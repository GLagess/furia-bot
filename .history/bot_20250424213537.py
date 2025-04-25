from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters
from handlers import cadastro, menu

def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # Adicionar o handler de CallbackQuery (cliques nos botões)
    app.add_handler(menu.button_handler)

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
    app.run_polling()

if __name__ == "__main__":
    main()
