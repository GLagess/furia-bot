import re
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, ConversationHandler
from services.database import salvar_usuario, usuario_existe

from utils.validations import validar_nome, validar_idade, validar_email

NOME, IDADE, CIDADE, EMAIL, INTERESSES = range(5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    if usuario_existe(user_id):
        await update.message.reply_text("✅ Você já está cadastrado! Use os botões para navegar.")
        return ConversationHandler.END

    await update.message.reply_text("👋 Olá! Vamos fazer seu cadastro para entrar no universo da FURIA.\nQual o seu nome?")
    return NOME


async def get_nome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    nome = update.message.text.strip()
    if not validar_nome(nome):
        await update.message.reply_text("❌ Nome inválido. Digite novamente, apenas letras.")
        return NOME
    context.user_data["nome"] = nome
    await update.message.reply_text("👍 Agora me diga sua idade:")
    return IDADE

async def get_idade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    idade = update.message.text.strip()
    if not validar_idade(idade):
        await update.message.reply_text("❌ Idade inválida. Digite um número maior ou igual a 10.")
        return IDADE
    context.user_data["idade"] = int(idade)
    await update.message.reply_text("🏙️ Qual sua cidade e estado? (ex: Teresina - PI)")
    return CIDADE

async def get_cidade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    cidade = update.message.text.strip()
    if len(cidade) < 3:
        await update.message.reply_text("❌ Cidade/Estado inválido. Tente novamente.")
        return CIDADE
    context.user_data["cidade"] = cidade
    await update.message.reply_text("📧 Qual o seu e-mail?")
    return EMAIL

async def get_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    email = update.message.text.strip()
    if not validar_email(email):
        await update.message.reply_text("❌ E-mail inválido. Digite novamente.")
        return EMAIL
    context.user_data["email"] = email

    keyboard = [
        [KeyboardButton("🎮 Esportes Eletrônicos"), KeyboardButton("⚽ Esportes Físicos")],
        [KeyboardButton("🌟 Influenciadores da FURIA"), KeyboardButton("🧠 Curiosidades do Time")]
    ]
    await update.message.reply_text(
        "🔍 Quais assuntos da FURIA você mais curte? Escolha uma opção abaixo:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
    return INTERESSES

async def get_interesses(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["interesses"] = update.message.text
    data = context.user_data
    user_id = update.effective_user.id
    salvar_usuario(user_id, data)


    await update.message.reply_text(
        f"✅ Cadastro finalizado! 👇 Suas informações:\n\n"
        f"👤 Nome: {data['nome']}\n"
        f"🎂 Idade: {data['idade']}\n"
        f"🏙️ Cidade: {data['cidade']}\n"
        f"📧 E-mail: {data['email']}\n"
        f"🎯 Interesse: {data['interesses']}\n\n"
        f"Agora é só explorar o conteúdo! 😎"
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Cadastro cancelado. Você pode começar novamente com /start.")
    return ConversationHandler.END
