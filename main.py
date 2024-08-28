from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, LabeledPrice, PreCheckoutQuery
import asyncio

TOKEN = '' # SCRIVI QUI IL TOKEN DEL TUO BOT
PAYMENT_TOKEN = '' # SCRIVI QUI IL TOKEN DI PAGAMENTO LIVE / TEST

AIUTOMSG = '''Comandi Disponibili:
/start
/help
/keyboard
/remove_keyboard
/inline_keyboard
/messaggio_formattato
/photo
/location
/payment'''

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(['start'])
async def start(message: Message):
    chat_id = message.chat.id
    nome = message.from_user.full_name
    await bot.send_message(chat_id, f'Benvenuto/a {nome}')

@bot.message_handler(['help'])
async def aiuto(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, AIUTOMSG)

@bot.message_handler(['keyboard', 'remove_keyboard'])
async def keyboard(message: Message):
    chat_id = message.chat.id
    if message.text == '/keyboard':
        kb = ReplyKeyboardMarkup(True)
        kb.add('bottone 1', 'bottone 2')
        kb.add('bottone 3')
        await bot.send_message(chat_id, 'Ecco la tastiera', reply_markup=kb)
    elif message.text == '/remove_keyboard':
        await bot.send_message(chat_id, 'Rimozione tastiera', reply_markup=ReplyKeyboardRemove())

@bot.message_handler(['inline_keyboard'])
async def inline(message: Message):
    chat_id = message.chat.id
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Bottone 1', 'https://fiverr.com'),
        InlineKeyboardButton('Bottone 2', callback_data='alertmsg')
    )
    await bot.send_message(chat_id, "Tastiera Inline", reply_markup=markup)

@bot.callback_query_handler()
async def callback(call: CallbackQuery):
    if call.data == 'alertmsg':
        await bot.answer_callback_query(call.id, 'Messaggio Pop up', show_alert=True)

@bot.message_handler(['messaggio_formattato'])
async def msg_formattato(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    MSG_FORMATTATO = '''*Messaggio in grassetto*
_testo corsivo_
[Link](https://fiverr.com/)
[menzione in linea di un utente](tg://user?id={})'''
    await bot.send_message(chat_id, MSG_FORMATTATO.format(user_id), 'markdown', disable_web_page_preview=True) # disable_web_page_preview -> disabilita la preview del sito web inviato nel messaggio

@bot.message_handler(['photo'])
async def photo(message: Message):
    chat_id = message.chat.id
    await bot.send_photo(chat_id, "https://fiverr-res.cloudinary.com/npm-assets/layout-service/fiverr-og-logo.5fd6463.png", 'Immagine di test!')

@bot.message_handler(['location'])
async def location(message: Message):
    chat_id = message.chat.id
    await bot.send_location(chat_id, 45.4654219, 9.1859243)

@bot.message_handler(['payment'])
async def payment(message: Message):
    chat_id = message.chat.id
    await bot.send_invoice(
        chat_id,
        'Test di pagamento',
        'Descrizione su test di pagamento',
        'payload-test',
        PAYMENT_TOKEN,
        'EUR',
        [LabeledPrice('Oggetto da pagare', 150)]
    )

@bot.pre_checkout_query_handler(lambda x: True)
async def pre_checkout(check: PreCheckoutQuery):
    try:
        await bot.answer_pre_checkout_query(check.id, True)
    except:
        await bot.answer_pre_checkout_query(check.id, False, 'Si è verificato un errore!')

@bot.message_handler(content_types=['successful_payment'])
async def pagamento(message: Message):
    chat_id = message.chat.id
    dati_pagamento = message.successful_payment
    #print(dati_pagamento) # se vuoi visualizzare i dettagli di pagamento
    await bot.send_message(chat_id, 'Pagamento effettuato con successo!')

asyncio.run(bot.polling())