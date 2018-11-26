from google.cloud import firestore
from pechinchator_scraper.firestore import FirestoreClient
from scrapy.utils.project import get_project_settings
from tasks.users_watch_list import UsersWatchList

settings = get_project_settings()
db = FirestoreClient.connect()

watchlist = UsersWatchList()

class FirestorePipeline:

    @classmethod
    def from_crawler(cls, crawler):
        if crawler.spider.name == "kabum":
            cls.ref = db.collection("products_beta")
        else:
            cls.ref = db.collection(settings["GCS_COLLECTION_NAME"])
        return cls()

    def process_item(self, item, _spider):
        thread_doc = self.ref.document(item.id)

        self.__create_or_update_thread(thread_doc, dict(item))
        return item

    def __create_or_update_thread(self, document, params):
        thread_snapshot = document.get()
        thread_exists = thread_snapshot.exists

        if thread_exists:
            has_changes = self.__check_for_changes(params, thread_snapshot.to_dict())
            if has_changes:
                params.update({"updated_at": firestore.SERVER_TIMESTAMP})
                document.set(params, {"merge": True})
        else:
            params.update({
                "created_at": firestore.SERVER_TIMESTAMP,
                "updated_at": firestore.SERVER_TIMESTAMP,
            })
            document.set(params)
            watchlist.check(params)

    @staticmethod
    def __check_for_changes(old_values, new_values):
        if old_values["replies_count"] != new_values["replies_count"]:
            return True

        return False
