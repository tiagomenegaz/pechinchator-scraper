from pechinchator_scraper.firestore import FirestoreClient
from google.cloud import firestore
from dotenv import load_dotenv
import telebot
import os
import time
from tasks.utils import Utils

load_dotenv()

db = FirestoreClient.connect()
users_ref = db.collection("users")


bot = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))


@bot.message_handler(commands=['watch'])
def cmd_add_product_to_watch_list(message):
    bot.send_chat_action(message.chat.id, 'typing')
    product_name = message.text.split(' ', 1)[1]
    bot.reply_to(message, "Opa! vou adicionar {} na sua lista, demorô já é?".format(product_name))
    user_ref = find_or_create_user(message.chat.id, message.chat.username)
    add_product_to_watch_list(user_ref, product_name)
    bot.send_message(message.chat.id, "Certinho! Quando houver alguma oferta eu irei te avisar, tá bom? =)")


def find_or_create_user(chat_id, username):
    user_ref = users_ref.document(str(chat_id))

    if not user_ref.get().exists:
        user_ref.set({"username": username, "added_at": firestore.SERVER_TIMESTAMP})

    return user_ref


def add_product_to_watch_list(user_ref, product_name):
    sanitized_message = Utils.strip_accents(product_name).lower().strip()
    user_products_ref = user_ref.collection("products")
    user_products_ref.document(sanitized_message).set({
        "name": sanitized_message,
        "added_at": firestore.SERVER_TIMESTAMP,
    })

bot.threaded=False

while True:
    try:
        bot.polling(none_stop=True, interval=1)
    except Exception as e:
        time.sleep(5)
