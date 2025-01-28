from dataclasses import dataclass


@dataclass
class MessageModel:
    user_id: int
    username: str
    text: str
