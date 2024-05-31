import chromadb
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings


class ChromaProvider:
    def __init__(self):
        persistent_client = chromadb.PersistentClient()
        persistent_client.get_or_create_collection("collection_name")
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.session = Chroma(
            client=persistent_client,
            collection_name="collection_name",
            embedding_function=embedding_function,
        )

    def get_session(self):
        return self.session
