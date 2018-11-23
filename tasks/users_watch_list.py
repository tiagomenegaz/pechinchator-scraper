from pechinchator_scraper.firestore import FirestoreClient
from dotenv import load_dotenv
from tasks.utils import Utils
import os
import telebot
load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY"))


class UsersWatchList:

    MESSAGE = """
    DEU MATCH! Nova oferta achada com a palavra-chave <b> {product_name} </b>! \n
    
    <b>{title} </b>\n
    {url}
    """

    def __init__(self):
        self.__db = FirestoreClient.connect()
        self.threads_ref = self.__db.collection("threads")
        self.users_docs = list(self.__db.collection("users").get())


    def check(self, product):
        sanitized_product_title = Utils.strip_accents(product["title"]).lower().split()
        for user_doc in self.users_docs:
            products_ref = user_doc.reference.collection("products").get()

            for product_ref in products_ref:
                if product_ref.id in sanitized_product_title:
                    formatted_message = self.MESSAGE.format(
                        product_name=product_ref.id,
                        title=product["title"],
                        url=product["url"],
                        content_html=product["content_html"]
                    )
                    bot.send_message(
                        user_doc.id,
                        formatted_message,
                        parse_mode='HTML'
                    )


if __name__ == "__main__":
    service = UsersWatchList()
    service.check({
        "title": "BLA",
        "content_html": '''<blockquote class="postcontent restore ">							Em até 20x no cartão submarino.<br><br><a href="https://www.submarino.com.br/produto/133284449/notebook-gamer-acer-predator-g3-572-75l9-intel-core-i7-16gb-geforce-gtx-1060-com-6gb-2tb-tela-ips-full-hd-15-6-windows-10-preto?voltagem=BIVOLT&amp;franq=AFL-03-460&amp;opn=AFLNOVOSUB&amp;loja=03" target="_blank">https://www.submarino.com.br/produto...OVOSUB&amp;loja=03</a>						</blockquote>''',
        "url": "https://www.hardmob.com.br/threads/655693-Amazon-Ebooks-Gratis-Amazon"
    })
