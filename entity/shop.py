from typing import Dict

from entity.base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int, max_unique_items: int):
        self.max_unique_items = max_unique_items
        super().__init__(items, capacity)

    def add(self, name: str, qnt: int) -> None:
        if self.get_unique_items_count() >= self.max_unique_items:
            pass

        super().add(name, qnt)

