class VectorBaseWrapper:
    def insert_doc_info(self, doc_id: int, doc_vectors: list) -> None:
        pass

    def delete_doc(self, doc_id: int) -> None:
        pass

    def get_doc_vectors(self, doc_id: int) -> list:
        pass

    def get_closest_responses(self, doc_id, message_vector) -> list:
        doc_vectors = self.get_doc_vectors(doc_id)
