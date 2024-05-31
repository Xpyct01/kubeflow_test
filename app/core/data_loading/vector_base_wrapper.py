from langchain_text_splitters import CharacterTextSplitter
from core.providers.chroma_provider import ChromaProvider


class VectorBaseWrapper:
    def __init__(self, provider: ChromaProvider):
        self.session = provider.get_session()

    def insert_doc_info(self, doc_content: list) -> None:
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(doc_content)
        self.db.add_documents(docs)

    def delete_doc(self, doc_id: str) -> None:
        self.db.delete(list(doc_id))

    def get_retriever(self, doc_id: str):
        retriever = self.db.as_retriever(search_kwargs={"doc_id": doc_id})
        return retriever
