from gotrue import SyncSupportedStorage
from flask import session

class FlaskSessionStorage(SyncSupportedStorage):
    def __init__(self):
        self.storage = session

    def get_item(self, key: str) -> str | None:
        return self.storage.get(key)

    def set_item(self, key: str, value: str) -> None:
        self.storage[key] = value

    def remove_item(self, key: str) -> None:
        self.storage.pop(key, None)
