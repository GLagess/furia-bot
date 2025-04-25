from telegram import Update
from telegram.ext import ContextTypes

async def show_esports(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Exemplo de resposta para o botão "Esportes Eletrônicos"
    await update.message.reply_text(
        "🎮 Aqui estão os Esportes Eletrônicos da FURIA:\n"
        "1. CS:GO\n"
        "2. Valorant\n"
        "3. Rainbow Six Siege"
    )

async def show_physical_sports(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Exemplo de resposta para o botão "Esportes Físicos"
    await update.message.reply_text(
        "⚽ FURIA também está envolvida com Esportes Físicos como a Kings League."
    )

async def show_influencers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Exemplo de resposta para o botão "Influenciadores da FURIA"
    await update.message.reply_text(
        "🌟 Conheça os influenciadores da FURIA nas redes sociais:\n"
        "1. [Influenciador 1](link)\n"
        "2. [Influenciador 2](link)\n"
        "3. [Influenciador 3](link)"
    )

async def show_team_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Exemplo de resposta para o botão "Curiosidades do Time"
    await update.message.reply_text(
        "🧠 FURIA é um time brasileiro de eSports, fundado em 2017. Desde então, tem conquistado diversos títulos no cenário global."
    )
