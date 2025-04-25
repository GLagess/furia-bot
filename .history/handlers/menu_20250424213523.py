from telegram import Update
from telegram.ext import ContextTypes

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Confirma o clique

    if query.data == "esports":
        # Mostra o submenu de jogos de Esportes Eletrônicos
        keyboard = [
            [InlineKeyboardButton("LOL", callback_data="lol"),
             InlineKeyboardButton("CS:GO", callback_data="csgo")],
            [InlineKeyboardButton("R6", callback_data="r6"),
             InlineKeyboardButton("Valorant", callback_data="valorant")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.message.reply_text(
            "Escolha um jogo de Esportes Eletrônicos:",
            reply_markup=reply_markup
        )

    elif query.data == "physical_sports":
        await update.callback_query.message.reply_text("FURIA participa da Kings League!")
    elif query.data == "influencers":
        await update.callback_query.message.reply_text("Conheça os influenciadores da FURIA!")
    elif query.data == "about_furia":
        await update.callback_query.message.reply_text("FURIA é um time brasileiro de eSports fundado em 2017.")

    # Respostas específicas para os jogos
    elif query.data == "lol":
        await update.callback_query.message.reply_text("🔥 FURIA no LOL: Line-up: [Jogadores] | Campeonatos: [Campeonatos]")
    elif query.data == "csgo":
        await update.callback_query.message.reply_text("🔥 FURIA no CS:GO: Line-up: [Jogadores] | Campeonatos: [Campeonatos]")
    elif query.data == "r6":
        await update.callback_query.message.reply_text("🔥 FURIA no R6: Line-up: [Jogadores] | Campeonatos: [Campeonatos]")
    elif query.data == "valorant":
        await update.callback_query.message.reply_text("🔥 FURIA no Valorant: Line-up: [Jogadores] | Campeonatos: [Campeonatos]")

# Adicionar o CallbackQueryHandler para gerenciar os cliques
from telegram.ext import CallbackQueryHandler
button_handler = CallbackQueryHandler(button_click)
