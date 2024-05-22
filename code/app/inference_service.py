from fastapi import FastAPI
from code.database.utils.HistoryBaseWrapper import HistoryBaseWrapper
from code.database.utils.UserBaseWrapper import UserBaseWrapper
from code.database.urils.VectorBaseWrapper import VectorBaseWrapper
from code.ml.llm.core import LLMService
from code.ml.ocr.core import OCRService
from code.ml.rag.core import RagService
from code.ml.embedding.core import EmbeddingService


app = FastAPI()
history_base_wrapper = HistoryBaseWrapper()
user_base_wrapper = UserBaseWrapper()
vector_base_wrapper = VectorBaseWrapper()
llm_service = LLMService()
ocr_service = OCRService()
rag_service = RagService()
embedding_service = EmbeddingService()


@app.post("/new_user")
async def new_user():
    user_base_wrapper.new_user()
    return {"message": "Hello World"}


@app.delete("/delete_user")
async def delete_user(user_id: int):
    user_base_wrapper.delete_user(user_id)
    return {"message": "Hello World"}


@app.post("/new_doc")
async def new_doc(doc):
    doc_content = ocr_service.get_doc_content(doc)
    doc_parts = rag_service.get_doc_parts(doc_content)
    doc_vectors = embedding_service.get_embeddings(doc_parts)
    history_base_wrapper.create_new_doc_history()
    vector_base_wrapper.insert_doc_info(doc_vectors)
    return {"message": "Hello World"}


@app.delete("/delete_doc")
async def delete_doc(user_id: int):
    history_base_wrapper.delete_doc(user_id)
    vector_base_wrapper.delete_doc(user_id)
    return {"message": "Hello World"}


@app.get("/get_user_docs")
async def get_user_docs(user_id: int):
    history_base_wrapper.get_user_docs(user_id)
    return {"message": "Hello World"}


@app.post("/send_message")
async def send_message(doc_id: str, message: str):
    message_history = history_base_wrapper.get_doc_history(doc_id)
    message_vector = embedding_service.get_embeddings([message])[0]
    closest_responses = vector_base_wrapper.get_closest_responses(doc_id, message_vector)
    modified_prompt = llm_service.get_modified_prompt(closest_responses, message)
    response = llm_service.send_message(message_history, modified_prompt)
    history_base_wrapper.update_doc_history(doc_id, response)
    return {"message": "Hello World"}
