from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI


contextualize_q_system_prompt = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""
qa_system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""


class RagService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def get_history_aware_retriever(self, llm, retriever):
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        history_aware_retriever = create_history_aware_retriever(
            llm, retriever, contextualize_q_prompt
        )
        return history_aware_retriever

    def get_question_answering_chain(self, llm):
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
        return question_answer_chain

    def get_conversational_rag_chain(self, retriever, message_history):
        history_aware_retriever = self.get_history_aware_retriever(self.llm, retriever)
        question_answer_chain = self.get_question_answering_chain(self.llm)
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            message_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )
        return conversational_rag_chain

    def get_rag_response(self, conversational_rag_chain, message):
        rag_response = conversational_rag_chain.invoke(
            {"input": message}
        )["answer"]
        return rag_response
