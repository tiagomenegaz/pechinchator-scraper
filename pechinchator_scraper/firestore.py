import json

from google.oauth2 import service_account
from google.cloud import firestore
from .settings import GCS_CREDENTIALS, GCS_PROJECT_ID


class FirestoreClient:

    @classmethod
    def connect(cls):
        credentials = service_account.Credentials.from_service_account_info(
            info=json.loads(GCS_CREDENTIALS)
        )
        db = firestore.Client(credentials=credentials, project=GCS_PROJECT_ID)

        return db
