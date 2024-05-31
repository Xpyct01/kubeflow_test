from typing import List
from core.providers.mongo_provider import MongoProvider


class HistoryBaseWrapper:
    def __init__(self, provider: MongoProvider):
        self.session = provider.get_session()

    def create_new_doc_history(self, title: str) -> None:
        self.session.insert_one({"title": title, "message_history": []})

    def delete_doc(self, doc_id: int) -> None:
        self.session.delete_one({"_id": doc_id})

    def get_doc_history(self, doc_id: int) -> List[str]:
        history = self.session.find_one({"_id": doc_id})
        return history["message_history"]

    def update_history(self, doc_id: int, message: str) -> None:
        history = self.get_doc_history(doc_id)
        history.append(message)
        self.session.update_one({"_id": doc_id}, {"$set": {"message_history": history}})
