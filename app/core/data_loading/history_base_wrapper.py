from typing import List


class HistoryBaseWrapper:
    def __init__(self):
        pass

    def create_new_doc_history(self, user_id: int, title: str, content: str) -> None:
        last_doc_id = ...
        new_doc_id = last_doc_id + 1

    def delete_doc(self, doc_id: int) -> None:
        pass

    def get_doc_history(self, doc_id: int) -> List[str]:
        pass

    def update_history(self, doc_id: int, message: str) -> None:
        pass
