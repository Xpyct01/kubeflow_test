from core.providers import PostgresProvider
from core.user_base.schema import User, Document


class UserBaseWrapper:
    def __init__(self, provider: PostgresProvider):
        self.session = provider.get_session()

    def create_new_user(self, user_type: str):
        new_log = User(type=user_type)
        self.session.add(new_log)
        self.session.commit()

    def add_document_to_user(self, user_id):
        document = Document(user_id=user_id)
        self.session.add(document)
        self.session.commit()

    def delete_user(self, user_id: int) -> str:
        user = self.session.query(User).filter_by(id=user_id).one()
        self.session.delete(user)
        self.session.commit()

    def delete_document(self, document_id: int) -> str:
        user = self.session.query(Document).filter_by(id=document_id).one()
        self.session.delete(user)
        self.session.commit()

    def get_user_docs(self, user_id: int) -> dict:
        docs = self.session.query(Document).filter_by(id=user_id).all()
        output_data = {"id": docs.id}
        return output_data
