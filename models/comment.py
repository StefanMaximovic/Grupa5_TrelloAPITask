from dataclasses import dataclass

@dataclass
class Comment:
    id: str
    idMemberCreator: str
    date: str
    text: str