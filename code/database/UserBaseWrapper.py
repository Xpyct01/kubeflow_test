from typing import List


class UserBaseWrapper:
    def create_new_user(self) -> None:
        last_user_id = ...
        new_user_id = last_user_id + 1

    def delete_user(self, user_id: int) -> None:
        pass

    def get_user_docs(self, user_id: int) -> List[str]:
        pass
