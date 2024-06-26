from fastapi import FastAPI
from app.core.data_loading.history_base_wrapper import HistoryBaseWrapper
from app.core.data_loading.user_base_wrapper import UserBaseWrapper
from core.data_loading.vector_base_wrapper import VectorBaseWrapper
from ml.ocr_service import OCRService
from ml.rag_service import RagService
from core.providers.postgres_provider import PostgresProvider
from core.providers.chroma_provider import ChromaProvider
from core.providers.mongo_provider import MongoProvider
from core.config import CONFIG


app = FastAPI()
history_base_wrapper = HistoryBaseWrapper(MongoProvider(CONFIG))
user_base_wrapper = UserBaseWrapper(PostgresProvider(CONFIG))
vector_base_wrapper = VectorBaseWrapper(ChromaProvider())
ocr_service = OCRService()
rag_service = RagService()


@app.post("/new_user")
async def new_user(data: dict) -> dict:
    user_type = data["type"]
    user_base_wrapper.create_new_user(user_type)
    return {"message": "success"}


@app.delete("/delete_user")
async def delete_user(data: dict) -> dict:
    user_id = data["user_id"]
    user_base_wrapper.delete_user(user_id)
    return {"message": "success"}


@app.post("/new_doc")
async def new_doc(data: dict) -> dict:
    images_list = data["images_list"]
    doc_title = data["doc_title"]
    doc_content = ocr_service.get_doc_content(images_list)
    history_base_wrapper.create_new_doc_history(doc_title)
    vector_base_wrapper.insert_doc_info(doc_content)
    return {"message": "success"}


@app.delete("/delete_doc")
async def delete_doc(data: dict) -> dict:
    doc_id = data["doc_id"]
    user_base_wrapper.delete_document(doc_id)
    history_base_wrapper.delete_doc(doc_id)
    vector_base_wrapper.delete_doc(doc_id)
    return {"message": "success"}


@app.get("/get_user_docs")
async def get_user_docs(data: dict) -> dict:
    user_id = data["user_id"]
    user_base_wrapper.get_user_docs(user_id)
    return {"message": "success"}


@app.post("/send_message")
async def send_message(data: dict) -> dict:
    doc_id = data["doc_id"]
    message = data["message"]
    message_history = history_base_wrapper.get_doc_history(doc_id)
    retriever = vector_base_wrapper.get_retriever(doc_id)
    conversational_rag_chain = rag_service.get_conversational_rag_chain(retriever, message_history)
    rag_response = rag_service.get_rag_response(conversational_rag_chain, message)
    return {"message": rag_response}
