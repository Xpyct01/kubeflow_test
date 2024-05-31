from langchain_chroma import Chroma
import chromadb
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter


class VectorBaseWrapper:
    def __init__(self):
        persistent_client = chromadb.PersistentClient()
        persistent_client.get_or_create_collection("collection_name")
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(
            client=persistent_client,
            collection_name="collection_name",
            embedding_function=embedding_function,
        )

    def insert_doc_info(self, doc_content: list) -> None:
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(doc_content)
        self.db.add_documents(docs)

    def delete_doc(self, doc_id: str) -> None:
        self.db.delete(list(doc_id))

    def get_retriever(self, doc_id: str):
        retriever = self.db.as_retriever(search_kwargs={"doc_id": doc_id})
        return retriever
