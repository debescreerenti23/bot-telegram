import random
import re  # Usaremos esto para buscar palabras exactas más fácil
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# --- CONFIGURACIÓN ---
TOKEN = "8609803094:AAGkU_FrzhOjjgWQx-tPAuPnWqonALZg6y8" # Recuerda usar el nuevo si hiciste /revoke

USUARIOS_VIP = ["javilindjjj", "usuario2"]

FRASES_VIP = [
    "¡Menudos ladrones los compra-árbitros del VarCelona!",
    "En todos los barrios hay un Mercadona y un tonto con la camiseta del Barcelona",
    "Estos le dan el 10 y las llaves del club a un moro, vaya memeclub",
    "Feliz 2-8 del mes que sea, subnormal",
    "Penaltito para el Varcelona",
    "La Liga Negreira, la mejor del mundo",
    "Entre el Williams y el Michael vaya legión de subnormales y falta el pirkus que va y viene",
    "Del barcelona y con down, y luego dicen que el señor no castiga 2 veces"
]

# Frases cuando alguien mencione al club
FRASES_BARCA = [
    "¡Més que un club, un memeclub!",
    "Los botones de la camisa de Juan Lapuerta tienen más presion que los tornillos de un submarino",
    "¡Puta Barça y Puta Cataluña!",
    "El Camp Nou es el nuevo acuario de Barcelona",
    
]

async def monitor_grupo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.lower() if update.message.text else ""
    
    if not user or not text:
        return

    # 1. REVISAR SI ES UN USUARIO VIP
    username_actual = user.username.lower() if user.username else ""
    if username_actual in USUARIOS_VIP:
        respuesta_vip = random.choice(FRASES_VIP)
        await update.message.reply_text(f"@{user.username} {respuesta_vip}")
        return # Si ya le contestó por VIP, no hace falta que siga buscando

    # 2. REVISAR SI MENCIONAN AL BARCELONA (Palabras clave)
    # Buscamos 'barcelona' o 'barça' (o 'barca')
    palabras_clave = ["barcelona", "barça", "barca"]
    
    if any(palabra in text for palabra in palabras_clave):
        respuesta_barca = random.choice(FRASES_BARCA)
        await update.message.reply_text(respuesta_barca)

# --- ARRANQUE ---
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), monitor_grupo))
    
    print("El bot del Barça está en el campo... 🏃‍♂️⚽")
    app.run_polling()